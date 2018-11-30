import os
import random
random_max = 10000
random_min = 1
number = 10000
a =[0 for i in range(number)]    
for j in range(number):
    a[j] = random.randint(random_min,random_max)
#    print(a)
try:
    f = open('C:\\Users\\li199\\Desktop\\random_number.txt', 'r+')
    for i in range(number):
        temp = str(a[j]) + '\n'
        f.writelines(temp)
finally:
    if f:
        f.close()
#        try:
#            os.mkdir('C:\\Users\\li199\\Desktop')
#            os.mknod('C:\\Users\\li199\\Desktop\\random_number.txt')
#其实不用这么写，以写进行文打开件若不存在会新建，然而没有批量注释算了。
#f = open('C:\\Users\\li199\\Desktop\\random_number.txt', 'a')
#    print('test')
#    f.write('hello world')
#    for j in range(number):
#        f.writelines(a[j])
#        f.writelines('/n')
#for i in f
#   f.writelines(a[j])
#f.close