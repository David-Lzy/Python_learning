import numpy
import random
import xlrd
import json
#a = numpy.array([[1, 2], [3, 4]])
#print(a[1])
#print(a[:, 0])
#print(a[1][0])

#print(random.randint(0, 10) for i in range(3))
#print(random.randint(0, 0))

#print(numpy.zeros([5, 20], dtype='bool_'))

#a = numpy.append(None, a)

#b = numpy.array([1, 2, 3, 3])
#c = numpy.where(b == 3)
#print(c)

#print(len(c))
#data = xlrd.open_workbook('2018年中国研究生数学建模竞赛E题（最新版）\\附件1  问题1虚假航迹点数据.xls')
#print(data.sheets()[0])
lines = open('fake_track.dat', 'r').readlines()
print(lines)
flen = len(lines) - 1
#for i in range(flen):
#    lines[i] = json.loads(lines[i])
#print(lines)
#for i in range(flen):
#    lines[i]