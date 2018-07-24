Pro Autocorrelation_function, result, sub_function1 , sub_function2 , All_Frame_number , useful_length
    time_interval   =   0L
    mean1           =   mean(sub_function1)
    mean2           =   mean(sub_function2)
    for i =0L, size(sub_function1,/N_elements)-1  do begin
      sub_function1[i] = sub_function1[i] - mean1
    endfor
    for i =0L, size(sub_function2,/N_elements)-1  do begin
      sub_function2[i] = sub_function2[i] - mean2
    endfor
    ifunction       =   dblarr(All_Frame_number-time_interval) ; 用来减少计算量
    result          =   dblarr(useful_length)
    for time_interval   =   0L  ,   useful_length-1   do begin ;通过之前的预实验可知，计算时间关联函数到10000帧已经没有相关性了
        for i = 0L, All_Frame_number - time_interval - 1  do begin
            ifunction[i]    =   sub_function1[i+time_interval]  *  sub_function2[i]
        endfor
        result(time_interval)   =   mean(ifunction[*])
    endfor 
End