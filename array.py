# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:37:57 2022

@author: Karsyn
"""

import sys
import numpy as np

def array(x,y,z,t):
    numarray = np.array([x,y,z,t])
    print(type(numarray))
    mul=int(x)*int(y)*int(z)*int(t)
    print(mul)

array(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])