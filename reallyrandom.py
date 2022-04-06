# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:06:46 2022

@author: Karsyn
"""

import sys
import numpy as np

def reallyrandom(x,y,z):
        #x is the size of np.randint from 0 to 10
        #y is an integer you multiply randint by
        #z is index result of multiplication by
        
        x=int(x)
        y=int(y)
        z=int(z)
        np.random.seed(42)
        rand= np.random.randint(10, size=(x))
        rand2=y*rand
        
        try:
                print('Your random value is',rand2[z])
        except:
                pass
                
reallyrandom(sys.argv[1],sys.argv[2], sys.argv[3])