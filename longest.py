# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 16:30:23 2022

@author: Karsyn
"""

import sys

def longest(string):
        words= string.split()
        result= ''
        for word in words:
                if len(word) > len(result):
                        result= word
                        result=result.lower()
        print(f'The longest word is {result}')
        
longest(sys.argv[1])
                        
        