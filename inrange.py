# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 21:00:22 2022

@author: Karsyn
"""

import sys

def inrange(num):
        num=int(num)
        num2=num+4
        count = 0 
        numlist=[]
        for i in range(5000,8001):
                if i % num==0 and i %num2==0:
                        numlist.append(i)
        print(numlist)

inrange(sys.argv[1])