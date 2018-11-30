
#x = np.linspace(0, 2 * np.pi, 50)
#plt.plot(x, np.sin(x)) # 如果没有第一个参数 x，图形的 x 坐标默认为数组的索引
#plt.show()

#print ("你好，世界")
#box_block = 10
#color     = 5

#Simulation_box =[[[1 for i in range(box_block)] for i in range(box_block)] for i in range(color)]

#print (Simulation_box)
#plt.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)

#name = input ('input your name')   
#print('hello',name)

#a = 100
#if a >= 0: 
#    print(a)
#else:
#    print(-a)

#print(ord('A'))
#x = np.linspace(-np.py,np.pi,256,endpoint=ture)
#C = np.cos(x)
#S = np.sin(x)
#while 1:

# -*- coding: utf-8 -*-   
  
""" import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', animated=False)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show() """

'''import numpy as np  
import matplotlib.pyplot as plt  
# 动画需要导入该模块  
from matplotlib import animation  
# 定义动画的速度，通过改变这个变量的值改变动画速度  
speed = 0.3  
  
fig, ax = plt.subplots()  
x = np.arange(0, 2*np.pi, 0.01)  
line, = ax.plot(x, np.sin(x))  
  
# 每次执行时的函数，  
def animate(i):  
    line.set_ydata(np.sin(x + i * speed))  
    return line,  
  
# 动画初始的方法  
def init():  
    line.set_ydata(np.sin(x))  
    return line,  
  
# fig : 执行动画的图像  
# func : 动画的执行函数  
# frames : 表示多少次动画为一个循环  
# init_func : 动画的初始位置  
# interval : 动画执行的间隔  不能为小数,小数动画就不执行了,不知道是不是我的姿势不对  
# blit : Mac设置为False,设置为True会报错,根据错误提示如下，可以使用'TKAgg'代替  
# matplotlib.animation.BackendError: The current backend is 
# 'MacOSX'and may go into an infinite loop with blit turned on.  
# Either turn off blit or use an alternate backend, 
# for example, like 'TKAgg', using the following prepended to your source code:  
ani = animation.FuncAnimation(fig=fig,func=animate,frames=int(2*np.pi/speed),init_func=init,interval=1,blit=False)  
# 查看帮助文档  
#help(ani.save)  
# 可以将动画以mp4格式保存下来，但首先要保证你已经安装了ffmpeg 或者mencoder  
# ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])  
  
plt.show() '''
'''import numpy
a = [[1,2,3],[4,5,6]]
b = []
b = numpy.append(b,a)
print(b)'''

'''
import os
import sys
import numpy
import copy
import codecs
import shutil

in_file_location = 'C:\\Users\\li199\\Desktop\\Python_test\\Data\\Kappa2'+ '%' +'Gamma20_%Beta0.0%N4096_%Compare0%'
variable_number = 1
temp = 'test' + '\n'

in_file = codecs.open(in_file_location+'\\in.2dplasma', 'r+')#,encoding='ISO-8859-1')
lines = []
for line in in_file:
    lines.append(line)
in_file.close()


variable_number = lines.find('atom_style      atomic')
lines.insert(variable_number,temp)
lines.insert(variable_number,temp)
lines.insert(variable_number,temp)
lines.insert(variable_number,temp)
s = ''.join(lines)

#print(lines)

in_file = open(in_file_location+'\\py.2dplasma', 'w',encoding='ISO-8859-1')
in_file.write(s)
in_file.close()
'''

#a = 'Gamma20beta0.2'
#print(a.find('beta'))
#a = 'Kappa2\\Gamma300\\Beta0.0\\N16384\\Compare0\\'
#print('variable        Gamma           equal')
'''a = ['1','2']
for i in a:
    try:
        print(i)
    except:
        pass
import sys
f = open(sys.path[0] + 'log.txt', 'a')'''

import os
print(os.path.dirname(os.path.dirname(__file__)))
