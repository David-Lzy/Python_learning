Pro Data_Building ,  file_path , All_flux_data , All_Frame_number , useful_length , frame_to_omega , Normalized

    Kinetic_Energy_part     =   0
    Potential_Energy_part   =   1
    Collision_X_part        =   2
    build_data1             =   dblarr(2,useful_length)
    build_data2             =   dblarr(7,useful_length)
    itime                   =   dindgen(useful_length)
   
    Ek_sum_item             =   All_flux_data[Kinetic_Energy_part   ,*]
    Ep_sum_item_x           =   All_flux_data[Potential_Energy_part ,*]
    F_Yukawa_sum            =   All_flux_data[Collision_X_part ,*]
    itime                   =   itime * frame_to_omega
        
        Autocorrelation_function    ,   C_Lambda_kk     ,   Ek_sum_item       ,   Ek_sum_item       ,   All_Frame_number ,  useful_length
        Autocorrelation_function    ,   C_Lambda_pp     ,   Ep_sum_item_x     ,   Ep_sum_item_x     ,   All_Frame_number ,  useful_length
        Autocorrelation_function    ,   C_Lambda_cc     ,   F_Yukawa_sum      ,   F_Yukawa_sum      ,   All_Frame_number ,  useful_length
        Autocorrelation_function    ,   C_Lambda_kp     ,   Ek_sum_item       ,   Ep_sum_item_x     ,   All_Frame_number ,  useful_length
        Autocorrelation_function    ,   C_Lambda_kc     ,   Ek_sum_item       ,   F_Yukawa_sum      ,   All_Frame_number ,  useful_length
        Autocorrelation_function    ,   C_Lambda_pc     ,   Ep_sum_item_x     ,   F_Yukawa_sum      ,   All_Frame_number ,  useful_length
    
    C_Lambda  = C_Lambda_kk + C_Lambda_pp + C_Lambda_cc + 2 *( C_Lambda_kc + C_Lambda_pc + C_Lambda_kp )    

        build_data1[0,*] = itime
        build_data1[1,*] = C_Lambda    * Normalized  
        
        build_data2[0,*] = itime      
        build_data2[1,*] = C_Lambda_kk / C_Lambda[0] 
        build_data2[2,*] = C_Lambda_pp / C_Lambda[0] 
        build_data2[3,*] = C_Lambda_cc / C_Lambda[0]
        build_data2[4,*] = C_Lambda_kp / C_Lambda[0] 
        build_data2[5,*] = C_Lambda_kc / C_Lambda[0] 
        build_data2[6,*] = C_Lambda_pc / C_Lambda[0] 
        
    

        
        file_mkdir  ,file_path
        openw       ,data_building0 ,   file_path+'flux.txt'         ,/get_lun , width=400
            Printf  ,data_building0 ,   'Kinetic_part  Potential_part  Collision_X_part'
            Printf  ,data_building0 ,   All_flux_data
         free_lun   ,data_building0
            
        openw       ,data_building1 ,   file_path+'C_Lambda.txt'     ,/get_lun , width=400
            Printf  ,data_building1 ,   '           time           sum '
            printf  ,data_building1 ,   build_data1
        free_lun    ,data_building1

        openw       ,data_building2 ,   file_path+'C_Lambda_part.txt',/get_lun , width=400
            Printf  ,data_building2 ,   '           time           KK               PP              CC              KP              KC              PC'
            printf  ,data_building2 ,   build_data2
        free_lun    ,data_building2
        ;printf  ,data_building2 , FORMAT = '("The values are: ", 2("<", I1, ">"))',
End
