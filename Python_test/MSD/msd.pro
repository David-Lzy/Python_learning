pro msd
  starttime=systime(/second)
  N_Particles=4096L
  N_Frames=6000L  ;test change here
  xy_t=fltarr(2,N_particles,N_frames)
 ; Vxy_t=fltarr(2,N_particles,N_frames/100.0)

  path=''
  filename='H:\2018SD_Lammps\1D\ASD\path.txt'
  openr,unit,filename,/get_lun
  while ~eof(unit) do begin
    readf,unit,path
    read_data_Lammps,xy_t,N_particles,N_frames,path
    get_MSD,xy_t,N_particles, N_frames, path
    endtime=systime(/second)
    print,'running time is',(endtime-starttime)/60.0
  endwhile
  close, unit
end

pro get_MSD,xy_t,N_particles, N_frames, filepath
  Lx=SQRT(4096/(1.15*0.866))
  Ly=0.866*Lx
  hLx=0.5*Lx
  hLy=0.5*Ly
  Ncorr_length=3000L
  N_overlapping = 100L
  openw,11,filepath+'_MSDx.txt'
  openw,12,filepath+'_MSDy.txt'
  openw,13,filepath+'_MSD.txt'
  for istep = 0L, Ncorr_length-1 do begin
    number_overlap=0.0
    MSDsumx=0.0
    MSDsumy=0.0
    MSDsum=0.0
    for k=0L,long(N_frames-istep-1L),N_overlapping do begin
      MSD_tempx=0.0
      MSD_tempy=0.0
      MSD_temp=0.0
      for iparticle=0, N_particles-1 do begin
        deltax=abs(xy_t[0,iparticle,k+istep]-xy_t[0,iparticle,k])
        deltay=abs(xy_t[1,iparticle,k+istep]-xy_t[1,iparticle,k])
        if (deltax gt hLx) then deltax=abs(Lx-deltax)
        if (deltay gt hLy) then deltay=abs(Ly-deltay)
        MSD_tempx = MSD_tempx + deltax*deltax;+deltay*deltay
        MSD_tempy = MSD_tempy + deltay*deltay;+deltay*deltay
        MSD_temp=MSD_tempx+MSD_tempy
      endfor
      ;MSD_temp1 = mean((xy_t[0,*,k+istep]-xy_t[0,*,k])^2+(xy_t[1,*,k+istep]-xy_t[1,*,k])^2)
      ;;v_temp1 = mean(Vxy_t[0,*,k+istep]*Vxy_t[0,*,k])
      ;;v_temp2 = mean(Vxy_t[1,*,k+istep]*Vxy_t[1,*,k])
      MSDsumx=MSDsumx+MSD_tempx
      MSDsumy=MSDsumy+MSD_tempy
      MSDsum=MSDsumx+MSDsumy
      ;vsum2=vsum2+v_temp2
      number_overlap=number_overlap+1.0
    endfor
    printf,11,istep,',',MSDsumx/(4096.0*number_overlap);,',',vsum2/number_overlap
    printf,12,istep,',',MSDsumy/(4096.0*number_overlap);,',',vsum2/number_overlap
    printf,13,istep,',',MSDsum/(4096.0*number_overlap);,',',vsum2/number_overlap
    ;x-axis dimensionless units
    ;printf,11,istep,',',vsum1/number_overlap,',',vsum2/number_overlap
  endfor
  close,11
  close,12
  close,13
  print, 'End of the calculation for the MSD!'
end