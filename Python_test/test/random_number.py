import random
import numpy
random_max = 3
random_min = 1
number = 10000
N =[0 for i in range(3)]    
compare_number = 1
random_number = [] 

try:
    f = open('C:\\Users\\li199\\Desktop\\random_number.txt', 'r+')
    for i in range(number):
        temp = int(f.readline())
        random_number = numpy.append(random_number,temp)
finally:
    if f:
        f.close()
for i in range(compare_number):
    print('this is the %rth random number list' % (i))
    for j in range(3):
        N[j] = random.randint(random_min,random_max)
        print(int(random_number[N[j]]))
    