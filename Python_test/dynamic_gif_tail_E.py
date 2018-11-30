import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import sys

#force='0.54'	#sys.argv[1]
vmin=0.0		#float(sys.argv[2])
vmax=1.0		#float(sys.argv[3])
x_max=17
y_max=14

Nparticles=1024
Nframes=800
fps=60
N_addfig=50
frame_time=196.0		#1frame=***s


def creat_mp4(Nparticles,Nframes,fps,N_addfig,filepath,outname,frame_time,vmin,vmax,x_max,y_max):
	cmap = mpl.cm.rainbow				#scata.set_cmap('plasma')
	norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
	m = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)


	data=np.zeros([4,Nframes,Nparticles])  
	duration = (Nframes-N_addfig)*0.999/fps

	def read_data(filepath,Nframes,Nparticles,data):
	#simple=Nparticles+9
	#simple_1=simple-1
		with open(filepath) as file:
			iline=0
			iframe=0
			ipar=0
			for line in file:
				#list = line.strip('\n').split(' ')
				list = line.strip().split()
				#judge_line=iline%simple
				#if( judge_line > 8 ):
				#ipar=int(list[0])-1
				#data[0,iframe,ipar]=float(list[1])
				#data[1,iframe,ipar]=float(list[2])
				#data[2,iframe,ipar]=float(list[4])
				#data[3,iframe,ipar]=float(list[5])
				#data[2,iframe,ipar]=float(list[3])
				#data[3,iframe,ipar]=float(list[4])
				#print(list)
				ipar=int(list[5])
				data[0,iframe,ipar]=float(list[0])
				data[1,iframe,ipar]=float(list[1])
				data[2,iframe,ipar]=float(list[2])
				data[3,iframe,ipar]=float(list[3])
				#if(judge_line==simple_1):
				if(ipar == Nparticles - 1):
					iframe +=1
				#print(iframe,list)	
				if(iframe == Nframes):
					break
				iline +=1
		return data

	read_data(filepath,Nframes,Nparticles,data)
	#print(np.max(data[2,:,:]*data[2,:,:]+data[3,:,:]*data[3,:,:]))

	fig_mpl, ax = plt.subplots(1,figsize=(15,9)) #,facecolor='silver')
	plt.subplots_adjust(left=0.03,right=0.95, top=0.96, bottom=0.09 )
	##   plt.setp(ax.spines.values(), color='white')
	#fig_mpl.set(facecolor='black')
	
	i=0
	pos=np.transpose(data[0:2,i,:])     #data[0,i,:]
	col=data[2,i,:]*data[2,i,:]+data[3,i,:]*data[3,i,:]
	#C = m.set_array(yy)
	scata=ax.scatter(pos[:,0], pos[:,1],c=col,alpha=1,marker='o',s=6,cmap=cmap,norm=norm)
	position=fig_mpl.add_axes([0.96, 0.09, 0.01, 0.87])  #left,down,width,hight 
	fig_mpl.colorbar(scata,cax=position)		
	
	def make_frame(t):
		ax.clear()
		ax.set_xlim(-x_max,x_max)
		ax.set_ylim(-y_max,y_max)
		#plt.setp([ax.get_xticklines(), ax.get_yticklines(),ax.get_xticklabels(), ax.get_yticklabels()], color='w')
		#ax.set(facecolor='silver')
		i=int(t*fps)
		for e in range(0,N_addfig,3):
			pos=np.transpose(data[0:2,i,:])     #data[0,i,:]
			col=data[2,i,:]*data[2,i,:]+data[3,i,:]*data[3,i,:]
			#C = m.set_array(yy)
			#s=(e+1)*1.2
			s=8
			ax.scatter(pos[:,0], pos[:,1],c=col,alpha=1,marker='o',s=s,cmap=cmap,norm=norm)
			i=i+3
		ax.set_title('Time:'+str(round((i-1.0)/frame_time+0.001,2))+'s')	
		return mplfig_to_npimage(fig_mpl)
		

	animation =mpy.VideoClip(make_frame, duration = duration)
	animation.write_videofile(outname, fps=fps)
	

filepath=r'I:\Sci\Data\Substrate\1DPS\G300K2\P0.0\O_1.dat'
outname=r'I:\Sci\Data\Substrate\1DPS\G300K2\P0.0\WK\E_1.6s_f60.mp4'
creat_mp4(Nparticles,Nframes,fps,N_addfig,filepath,outname,frame_time,vmin,vmax,x_max,y_max)
