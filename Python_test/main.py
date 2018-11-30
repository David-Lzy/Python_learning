import math
import random
import matplotlib.pyplot as plt
import matplotlib.animation as Fun_movie
import numpy 

box_block  = 1000
radius     = math.floor(box_block/2)
location_X = math.floor(radius)
location_Y = math.floor(radius)
plt.axis([0, box_block, 0, box_block])
speed      = 0.3  
color      = 5
fig, ax    = plt.subplots()  
#Simulation_box =[[i for i in range(box_block)] for i in range(box_block)]
Simulation_box = numpy.zeros([box_block,box_block])
Simulation_box[radius,radius] = 1

#run_time = [1 for i in range(1000)]
#for compute_step in run_time
while  True :
#dot, =  ax.plot(location_X,location_Y)
#def init():
#    dot.set_xdata(location_X)
#    dot.set_ydata(location_Y)
#    return dot,
#def animate(i):
    sita1 = random.uniform(-math.pi , math.pi)
    sita2 = random.uniform(-math.pi , math.pi)
    location_X = math.floor(radius*(1+math.sin(sita1)))
    location_Y = math.floor(radius*(1+math.sin(sita2)))
    #plt.plot([location_X], [location_Y], 'ro')
    #plt.figure()
    while (1<=location_X)and(1<=location_Y)and(location_X<=box_block)and(location_Y<=box_block) :
        N = numpy.sum(Simulation_box[location_X-1:location_X+1,location_Y-1:location_Y+1])
        if N>0 :
            Simulation_box[location_X,location_Y] = 1
            #plt.plot([location_X], [location_Y], 'ro')
            #dot, = ax.plot(location_X,location_Y)
            dot.set_xdata(location_X)
            dot.set_ydata(location_Y)
            
        else :
            rand1 = random.uniform(-2 , 5)
            if rand1 > 0 :
                location_X = location_X + 1
            else :
                location_X = location_X - 1
            rand2 = random.uniform(-2 , 5)
            if rand2 > 0 :
                location_Y = location_Y + 1
            else :
                location_Y = location_Y - 1
    return dot,
    #break
#ani = Fun_movie.FuncAnimation(fig=fig,func=animate,frames=1,init_func=init,interval=1,blit=False)     
plt.show()    