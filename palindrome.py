# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 18:06:37 2022

@author: Karsyn
"""

import sys

def palindrome(word):
        newstring=''
        letterlist=['a','b','c','d','e','f','g','h','i',
                    'j','k','l','m','n','o','p','q','r','s',
                    't', 'u','v','w','x','y','z']
        word=word.lower()
        for letter in word:
                if letter in letterlist:
                        newstring=newstring+letter
        
        index=len(newstring)
        revers=''
        while index>0:
                revers+= newstring[index-1]
                index=index-1
        #revers=newstring[::-1]
        if revers == newstring:
                print("It's a palindrome!")
        else:
                print("It's not a palindrome!")

palindrome(sys.argv[1])
