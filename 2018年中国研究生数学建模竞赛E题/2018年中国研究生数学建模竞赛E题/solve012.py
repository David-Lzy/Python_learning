import time
import sympy 
import numpy 
start =time.clock()

radar = numpy.array([[80,0,0],[30,60,0],[55,110,0],[105,110,0],[130,60,0]])
fake = numpy.loadtxt('fake_track.dat')/1000 #unit km
x0, y0, z0, vx, vy, vz = sympy.symbols('x0 y0 z0 vx vy vz') #velocity km/h
def lines_solve(f0,radar0,fake0,f1,radar1,fake1,f2,radar2,fake2):
    #first radar x0 = radar[0] y0 = radar[1]  z0 = radar[2]
    t0,t1,t2 = f0/360, f1/360, f2/360 # unit to h

    #print(radar2,fake2)
    result = sympy.solve([
                 (x0+vx*t0-radar0[0])*(fake0[1]-radar0[1])-(y0+vy*t0-radar0[1])*(fake0[0]-radar0[0]),
                 (y0+vy*t0-radar0[1])*(fake0[2]-radar0[2])-(z0+vz*t0-radar0[2])*(fake0[1]-radar0[1]),
                 (x0+vx*t1-radar1[0])*(fake1[1]-radar1[1])-(y0+vy*t1-radar1[1])*(fake1[0]-radar1[0]),
                 (y0+vy*t1-radar1[1])*(fake1[2]-radar1[2])-(z0+vz*t2-radar1[2])*(fake1[1]-radar1[1]),
                 (x0+vx*t2-radar2[0])*(fake2[1]-radar2[1])-(y0+vy*t2-radar2[1])*(fake2[0]-radar2[0]),
                 (y0+vy*t2-radar2[1])*(fake2[2]-radar2[2])-(z0+vz*t2-radar2[2])*(fake2[1]-radar2[1])
                 ],
                 [x0, y0, z0, vx, vy, vz] , dict=True)

    return result  #result[x0],result[y0],result[z0],result[vx],result[vy],result[vz]

def get_points(result):
    points = {'check':False,'radar_frame':numpy.zeros([5,20],dtype ='bool_'),'xyz':[]}
    if result:
        V = result[0][vx]**2+result[0][vy]**2+result[0][vz]**2
        if 14400<=V<=32400:
            for iframe in range(20):
                t_h = iframe/360.0
                for iradar in range(5):
                    z_real = result[0][z0]+result[0][vz]*t_h
                    #print(z_real)
                    if 2<=z_real<=2.5:
                        x_real = result[0][x0]+result[0][vx]*t_h
                        y_real = result[0][y0]+result[0][vy]*t_h
                        if (abs((x_real-radar[iradar][0])*(fake[iframe][1]-radar[iradar][1])
                           /((y_real-radar[iradar][1])*(fake[iframe][0]-radar[iradar][0]))-1)<0.1 and
                           abs((x_real-radar[iradar][0])*(fake[iframe][2]-radar[iradar][2])
                           /((z_real-radar[iradar][2])*(fake[iframe][0]-radar[iradar][0]))-1)<0.1):
                            points['radar_frame'][iradar,iframe] = True
                if numpy.sum(points['radar_frame'])>=2:
                    points['check']=True
                    points['xyz']=result[0]
    return points
                    
                    

f0, radarID0 = 0, 0 #0-20,0-4
f1, radarID1 = 1, 1
f2, radarID2 = 2, 2
with open('.dat','w') as f:
    for f0 in range(20):
        for f1 in range(20):
            if f0==f1:continue
            for f2 in range(20):
                if f0==f2 or f1==f2:continue
                print(f0,f1,f2)
                result = lines_solve(f0,radar[radarID0],fake[f0],f1,radar[radarID1],fake[f0],f2,radar[radarID2],fake[f2])
                points = get_points(result)
                print(result)
                print('-'*40)
                f.write(str(f0)+','+str(f1)+','+str(f2)+'\n')
                f.write(str(result)+'\n')
                f.write('-'*30+'\n')
                if points['check']:
                    print(points)
                    f.write('find_solve')
                    f.write(str(points))


end = time.clock()
print('Running time: %s Seconds'%(end-start))
