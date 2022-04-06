# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 20:16:04 2022

@author: Karsyn
"""

import sys


def digits(number):
        number = str(number)
        count=0
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        for dig in number:
                if dig in numbers:
                        count=count+1
        print(count)
digits(sys.argv[1])