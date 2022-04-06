# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 19:59:14 2022

@author: Karsyn
"""

import sys
import pandas as pd

def presidents(x,y):
        df=pd.read_csv('president_heights.csv')

        heights=df['height(cm)']
        h2=heights.iloc[x:y]
        z=round(h2.mean(), 2)
        print(f'The average height of presidents number {x} to {y} is {z:.2f}')
        
presidents(int(sys.argv[1]),int(sys.argv[2]))