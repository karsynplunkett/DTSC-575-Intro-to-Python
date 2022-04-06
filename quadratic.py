# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 20:38:28 2022

@author: Karsyn
"""

import sys
import math

def quadratic(a,b,c):
        a=float(a)
        b=float(b)
        c=float(c)
        pos=(-1*b+ math.sqrt((b**2)-4*a*c))/(2*a)
        neg= (-1*b-math.sqrt((b**2)-4*a*c))/(2*a)
        print(f'The solutions are {pos:.2f} and {neg:.2f}')
        
quadratic(sys.argv[1],sys.argv[2],sys.argv[3])
#quadratic(2,4,1)
