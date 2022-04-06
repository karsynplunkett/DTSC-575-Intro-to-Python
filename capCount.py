# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:49:45 2022

@author: Karsyn
"""

import sys

def capCount(string):
        count=0
        index=0
        for i in range(len(string)):
                if string[i].isupper() == True:
                        index= index+i
                        count=count+1
        print(count)
        print(index)
capCount(sys.argv[1])
        