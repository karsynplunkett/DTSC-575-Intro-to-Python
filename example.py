# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:46:43 2022

@author: Karsyn
"""

def func(*, a, b, **kwargs):
    print(a)
    print(b)
    print(kwargs)

#func(a="aa",b="bb", c="cc")

def func2(*, a, b):
    print(a)
    print(b)
#func(a="aa", b="bb")

def classes(*args):
        print(args)
        
classes('dtscg560','dtsbds3')