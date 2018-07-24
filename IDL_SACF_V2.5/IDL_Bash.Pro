Pro IDL_Bash
    Gamma_                      =   20L
    test_time                   =   'Formal_analysis'
    useful_length               =   10000L
    Real_All_frame_number       =   10*10000UL
    file_number                 =   5
    skip_ratio                  =   0.0
    start_ratio                 =   0.0
    All_Particle_number         =   16384L
    frame_to_omega              =   0.113137
    data_path                   =   'G:\Data\without_analysis\' + test_time + '\'
    bash_path                   =   file_dirname(routine_filepath('IDL_Bash'))    
    single_file_frame_number    =   long64(Real_All_frame_number / file_number)
    all_frame_number            =   long64(Real_All_frame_number*(1-skip_ratio))
    Frame_number                =   long64(single_file_frame_number * (1-skip_ratio))
    start_point                 =   long64(single_file_frame_number * start_ratio)
    single_flux_data            =   dblarr(3,Frame_number)
    All_flux_data               =   dblarr(3,Real_All_frame_number) 
    Normalized                  =   (Gamma_^2/(All_Particle_number/2.0))*frame_to_omega
    ;在Data_Getting中已经对flux normalized，故只需一次frame到ogmega 
    file_path_temp              =   ' '
    file_path                   =   ' '
        
        time1   =   systime(/seconds)
        time    =   systime()
        print   ,   'Program start at ' , time
        openr   ,   path_getting    ,   bash_path + '\Bash.txt' , /get_lun 
          while ~eof(path_getting)  do begin
            time3   =   systime(/seconds)           
            readf       ,   path_getting  ,   file_path_temp
            file_path   =  data_path   + file_path_temp + '\'
            
                for i_file_number = 1 , file_number  do begin
                  
                    time5 = systime(/seconds)
                        IDL_Data_Getting    ,   file_path , single_flux_data , Frame_number , All_Particle_number , start_point , i_file_number , frame_to_omega 
                        All_flux_data[*,((i_file_number-1)*Frame_number):(i_file_number*Frame_number-1)] = single_flux_data
                    time6 = systime(/seconds)                    
                    time_spend3  =   STRTRIM(string(long(( time6 - time5 )/60)),2)
                    number  =   STRTRIM(string(i_file_number),2)                  
                    print  ,  number , 'th has been read , and cost ' , time_spend3 , ' minutes.'
                
                endfor
                
                analysis_path   =  data_path  + 'IDL_Basic_analysis\' + file_path_temp + '\'
                Data_Building       ,   analysis_path , All_flux_data , all_frame_number , useful_length , frame_to_omega , Normalized
            
            time4   =   systime(/seconds)
            time_spend1  =   STRTRIM(string(long((time4 - time3)/60)),2)
            print , file_path_temp ,' done ,and cost ' , time_spend1 , ' minutes.'
              
          endwhile
        free_lun,   path_getting
        
    time2       =   systime(/seconds)
    time_spend2 =    STRTRIM(string(long(( time2 - time1 )/3600)),2)
    print , 'All done , and cost '   , time_spend2 , ' hours.'
End