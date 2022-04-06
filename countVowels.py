# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:25:53 2022

@author: Karsyn
"""

import sys

def countVowels(string):
        templist=[]
        vowels=['a','e','i','o','u']
        count=0
        for letter in string:
                if letter in vowels and letter not in templist:       
                        count=count+1
                        templist.append(letter)
        print(count)

countVowels(sys.argv[1].lower())