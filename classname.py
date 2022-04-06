# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 19:53:32 2022

@author: Karsyn
"""
import sys

class person():
        def hello(self, name):
                self.name=name
                print('My name is '+ name,'and I am a ' + str(type(self).__name__))
person = person()
person.hello(sys.argv[1])
print(type(person))