# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 19:09:47 2022

@author: Karsyn
"""

class Cow:
        def speak(self):
                print('Moo')
        def eat(self):
                print('Yum')
                
class Holstein(Cow):
        def talk(self):
                super().speak()
print(issubclass(Cow, Holstein))