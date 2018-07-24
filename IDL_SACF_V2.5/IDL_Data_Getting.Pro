Pro IDL_Data_Getting    , file_path , All_data , All_Frame_number , All_Particle_number , start_point , i_file_number , frame_to_omega 
    speed_cpu               =   1000L
    All_data_temp           =   dblarr(3,All_Particle_number*speed_cpu)
    All_data_temp_temp      =   dblarr(3,All_Particle_number)
    heat_flux               =   dblarr(1,All_Frame_number)
    heat_flux_temp          =   dblarr(2,speed_cpu)
    real_heat_flux_temp     =   dblarr(speed_cpu)
    save_RAM                =   All_Frame_number/speed_cpu

    Velocity_X              =   0
    Velocity_Y              =   !NULL
    Kinetic_Energy          =   1
    Potential_Energy        =   2
    Collision_XX            =   !NULL
    Collision_YY            =   !NULL
    Collision_XY            =   !NULL
    Kinetic_Energy_part     =   0
    Potential_Energy_part   =   1
    Collision_X_part        =   2
 
    file_number           =   string(i_file_number)
    file_number           =   STRTRIM(file_number,2);去除两头空格
    Catch   ,   error
    IF error ne 0 then begin
      
          openr   ,   data_getting    ,   file_path + '2dp_EACF_' + file_number + '.lammpstrj' , /get_lun   ;get lun 相当于给前面的data_getting一个数
              Skip_Lun  ,   data_getting     ,   start_point*(All_particle_number + 9) , /Lines
              
              for iframe =0L  ,   save_RAM-1 do begin
                  for loop_time = 0L , speed_cpu-1 do begin
                      Skip_Lun  ,   data_getting     ,   9 , /Lines             
                      readf     ,   data_getting     ,   All_data_temp_temp
                      All_data_temp[ *,All_Particle_number*loop_time : All_Particle_number*(loop_time+1)-1 ] = All_data_temp_temp
                  endfor
                  location = iframe * speed_cpu 
                  for loop_time = 0L , speed_cpu-1 do begin
                      begin_part = All_Particle_number*loop_time
                      end_part   = All_Particle_number*(loop_time+1)-1
                      All_data[Kinetic_Energy_part ,   location + loop_time]  = total(All_data_temp[Velocity_X ,begin_part : end_part] * All_data_temp[Kinetic_Energy   ,begin_part : end_part])
                      All_data[Potential_Energy_part , location + loop_time]  = total(All_data_temp[Velocity_X ,begin_part : end_part] * All_data_temp[Potential_Energy ,begin_part : end_part])
                  endfor
      
              endfor
              All_data[Potential_Energy_part,*]   =   0.5 * All_data[Potential_Energy_part,*] * frame_to_omega
              All_data[Kinetic_Energy_part,*]     =   0.5 * All_data[Kinetic_Energy_part,*] * frame_to_omega
          free_lun,   data_getting
      
          openr   ,   data_getting2    ,   file_path + 'log.lammps' , /get_lun
              Skip_Lun    ,   data_getting2   , 77 , /Lines
              skip_lun    ,   data_getting2   , (i_file_number-1) * (All_Frame_number+29) , /Lines
              Skip_Lun    ,   data_getting2   , start_point , /Lines
              for iframe =0L  ,   save_RAM-1 do begin   
                  readf   ,   data_getting2   , heat_flux_temp
                  location = iframe * speed_cpu
                  for loop_time = 0L , speed_cpu-1 do begin
                      real_heat_flux_temp[loop_time] = All_Particle_number /2 * heat_flux_temp[1,loop_time] * frame_to_omega
                      i = location +loop_time
                      All_data[Collision_X_part,i]   =  - (All_data[Kinetic_Energy_part,i] + All_data[Potential_Energy_part,i]) +  real_heat_flux_temp[loop_time]
                  endfor
              endfor
          free_lun,   data_getting2  
      
      
          if (i_file_number le 1) then begin
              openw   ,   data_writing1   ,   file_path + 'flux.txt'    , /get_lun  , width=400
              printf  ,   data_writing1   ,   'Kinetic_part  Potential_part  Collision_X_part'
              free_lun,   data_writing1
          endif  
              openu   ,   data_writing2   ,   file_path + 'flux.txt'    , /get_lun  , width=400
              skip_lun,   data_writing2   ,   ((i_file_number-1) * All_Frame_number+1) , /Lines
              
              for iframe =0L  ,   All_Frame_number-1  do begin    
                  printf      ,   data_writing2   ,   All_data[Kinetic_Energy_part,iframe] , All_data[Potential_Energy_part,iframe] , All_data[Collision_X_part,iframe] 
              endfor
          free_lun,   data_writing2
          
    Endif
    
    openr   ,   data_getting    ,   file_path + 'flux.txt' , /get_lun
        skip_lun,   data_getting   ,   ((i_file_number-1) * All_Frame_number+1) , /Lines
        readf   ,   data_getting   ,   All_data
End
