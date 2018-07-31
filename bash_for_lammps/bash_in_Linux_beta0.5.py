#!/usr/bin/env python
import os
import sys
import time
import numpy
import copy
import codecs
import shutil
import random
import subprocess

Data_location = sys.path[0] + '/Data/ready_to_run/Formal_analysis/'

compare = []
compare_number = [i for i in range(0,10)]#从0到9左闭右开
compare_str = 'Compare'

beta = []
beta_number = [0.0,0.1,0.2,0.5,0.7,1.0]#[0.1*i for i in range(2,3)]
beta_str = 'Beta'

kappa = []
kappa_number = [2,]
kappa_str = 'Kappa'

gamma = []
gamma_number = ['300']#,'300']
gamma_str = 'Gamma'

particle_N = []
particle_N_number = ['16384']#'1024','4096',
particle_N_str = 'N'

str_paramter = [kappa_str,gamma_str,beta_str,particle_N_str,compare_str]

for i in compare_number:
    temp = compare_str + str(i)
    compare = numpy.append(compare,temp)

for i in gamma_number:
    temp = gamma_str + str(i)
    gamma = numpy.append(gamma,temp)

for i in beta_number:
    temp = beta_str + str(i)
    beta = numpy.append(beta,temp)

for i in particle_N_number:
    temp = particle_N_str + str(i)
    particle_N = numpy.append(particle_N,temp)

for i in kappa_number:
    temp = kappa_str + str(i)
    kappa = numpy.append(kappa,temp)

All_parameter = [kappa,gamma,beta,particle_N,compare]

All_path = ['']
win_path = ['']
for i in range(len(All_parameter)):
    path_number = len(All_path)
    parameter_number = len(All_parameter[i])
    temp1 = [['' for  a in range(path_number)] for b in  range(parameter_number)]
    temp2 = [['' for  a in range(path_number)] for b in  range(parameter_number)]
    for j in range(parameter_number):    
        for k in range(path_number):            
            temp1[j][k] = All_path[k]+All_parameter[i][j]+ '/' 
            temp2[j][k] = win_path[k]+All_parameter[i][j]+ '\\'           
    All_path = []
    win_path = [] 
    All_path = numpy.append(All_path,temp1)  
    win_path = numpy.append(win_path,temp2)

def modify_file(tfile,old,new):
    try:
        lines=open(tfile,'r').readlines()
        flen=len(lines)-1
        for i in range(flen):
            if old in lines[i]:
                lines[i]=lines[i].replace(old,new)
        open(tfile,'w').writelines(lines)       
    except Exception as e:
        print(e)

for i in range(len(All_path)):

    in_file_location = Data_location + All_path[i]
    try:
        os.makedirs(in_file_location)
    except Exception as e:
        print(e)
    shutil.copy(sys.path[0]+'/in.2dplasma',in_file_location)

    number_begin = [0] * len(str_paramter)
    number_end   = [0 for a in  range(len(str_paramter))]
    new_str      = '' 

    #print(All_path)

    for j in range(len(str_paramter)):
        number_begin[j] = All_path[i].find(str_paramter[j]) + len(str_paramter[j])          
    for j in range(len(str_paramter)-1):            
        number_end[j]   = All_path[i].find(str_paramter[j+1]) - 1       
    number_end[len(str_paramter)-1] = All_path[i][len(All_path[i])-1]
    
    for j in range(len(str_paramter)):
        #print(str_paramter[j])
        if  str_paramter[j] == 'N':

            old_str = 'region          box     block'
            if All_path[i][number_begin[j]:number_end[j]] == '1024':
                new_str = old_str + '           -16 16 -8 8 -0.3 0.3'
            elif All_path[i][number_begin[j]:number_end[j]] == '4096':
                new_str = old_str + '           -32 32 -16 16 -0.3 0.3'
            elif All_path[i][number_begin[j]:number_end[j]] == '16384':
                new_str = old_str + '           -64 64 -32 32 -0.3 0.3'                           
            modify_file(in_file_location+'in.2dplasma',old_str,new_str)

        if  str_paramter[j] == 'Compare':

            old_str = 'variable        random1'
            new_str = old_str + '\t\t\tequal' + '\t\t' +  str(random.randint(0,10000))
            modify_file(in_file_location+'in.2dplasma',old_str,new_str)

            old_str = 'variable        random2'
            new_str = old_str + '\t\t\tequal' + '\t\t' +  str(random.randint(0,10000))
            modify_file(in_file_location+'in.2dplasma',old_str,new_str)

            old_str = 'variable        random3'
            new_str = old_str + '\t\t\tequal' + '\t\t' +  str(random.randint(0,10000))
            modify_file(in_file_location+'in.2dplasma',old_str,new_str)

        else:

            old_str = 'variable        ' + str_paramter[j] 
            
            new_str = old_str + '\t\t\tequal' + '\t\t' + All_path[i][number_begin[j]:number_end[j]]
            #print(new_str)
            modify_file(in_file_location+'in.2dplasma',old_str,new_str) 


log_location = sys.path[0] + '/log.txt'
f = open(log_location, 'a+')
f.writelines('=========================================================\n')
f.writelines('this MD simulation start at ')
f.writelines( time.strftime("%Y-%m-%d %H:%M:%S \n", time.localtime()) )
f.writelines('All paramters list here\n')
for i in All_parameter:
    j = str(i)+'\n'
    f.writelines(j)
f.writelines('ALl Windows path ready to run list here\n')
f.writelines('*****************************************\n')
for i in win_path:
    j = str(i)+'\n'
    f.writelines(j)
f.writelines('******************************************\n')
f.close()


f = open(log_location, 'a+')
for i in range(len(All_path)):
    in_file_location = Data_location + All_path[i] 
    try:
        subprocess.call('mpirun -np 19 /home/dpmd0/lammps/src/lmp_ubuntu < in.2dplasma',shell=True,cwd=in_file_location)
        os.rename(in_file_location+'in.2dplasma',in_file_location+'py.in.2dplasma')
    except Exception as e:
        try:
            f.writelines('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
            f.writelines('sorry, it seems that something get wrong, and the wrong file is:\n')
            f.writelines(in_file_location)
            f.writelines('here is the deatials:\n')
            f.writelines(e)
            f.writelines('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
        except Exception :
            pass
f.writelines('All done, and this MD simulation finished at ')
f.writelines( time.strftime("%Y-%m-%d %H:%M:%S \n", time.localtime()) )
f.writelines('=========================================================\n')
f.close()