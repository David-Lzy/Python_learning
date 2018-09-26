import time
start =time.clock()
from sympy import *
def lines_solve(radar0,fake0,f1,radar1,fake1,f2,radar2,fake2):
    #first radar x0 = radar[0] y0 = radar[1]  z0 = radar[2]
    t1,t2 = f1/360, f2/360 # unit to h
    x0, y0, z0, vx, vy, vz = symbols('x0 y0 z0 vx vy vz') #velocity km/h
    #print(radar2,fake2)
    result = solve([
                 (x0+vx*t1-radar1[0])*(fake1[1]-radar1[1])-(y0+vy*t1-radar1[1])*(fake1[0]-radar1[0]),
                 (y0+vy*t1-radar1[1])*(fake1[2]-radar1[2])-(z0+vz*t2-radar1[2])*(fake1[1]-radar1[1]),
                 (x0+vx*t2-radar2[0])*(fake2[1]-radar2[1])-(y0+vy*t2-radar2[1])*(fake2[0]-radar2[0]),
                 (y0+vy*t2-radar2[1])*(fake2[2]-radar2[2])-(z0+vz*t2-radar2[2])*(fake2[1]-radar2[1]),
                 (x0-radar0[0])*(fake0[1]-radar0[1])-(y0-radar0[1])*(fake0[0]-radar0[0]),
                 (y0-radar0[1])*(fake0[2]-radar0[2])-(z0-radar0[2])*(fake0[1]-radar0[1]),
                 ],
                 [x0, y0, z0, vx, vy, vz])
    return result  #result[x0],result[y0],result[z0],result[vx],result[vy],result[vz]


radar0, fake0 = [-1,1,0], [1,1,0]
f1, radar1, fake1 = 1, [-1,1,0], [1,1,0]
f2, radar2, fake2 = 2, [-1,45,0], [1,2,50]
#for i in range(10000):
result = lines_solve(radar0,fake0,f1,radar1,fake1,f2,radar2,fake2)
print(result)

end = time.clock()
print('Running time: %s Seconds'%(end-start))
