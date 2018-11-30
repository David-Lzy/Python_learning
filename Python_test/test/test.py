import os
import time
import numpy
import copy
import codecs
import shutil
import random
import subprocess
in_file_location = os.path.dirname(__file__) + '\\test.txt'

def modify_file(tfile, old, new):
    try:
        lines = open(tfile, 'r').readlines()
        flen = len(lines) - 1
        for i in range(flen):
            if old in lines[i]:
                lines[i] = lines[i].replace(old, new)
        open(tfile, 'w').writelines(lines)
    except Exception as e:
        print(e)



modify_file(in_file_location , 'test', 'vfdbfdbdf')