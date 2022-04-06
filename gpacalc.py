# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 20:23:46 2022

@author: Karsyn
"""
import sys

def gpacalc(x,y,z,t):
        dict1={'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}
        x=x.upper()
        y=y.upper()
        z=z.upper()
        t=t.upper()
        avg= round((dict1[x]+dict1[y]+dict1[z]+dict1[t])/4, 2)
        print(f'My GPA is {avg:.2f}')

gpacalc(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
