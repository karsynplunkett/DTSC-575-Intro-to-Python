# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:12:37 2022

@author: Karsyn
"""


import pandas as pd

df1 = pd.read_csv('merge_practice.csv')
df2=pd.read_csv('pct_distribution.csv')

pd.read_csv('merge_practice.csv')

merged= df1.merge(df2, how='outer', on='Product')
print(merged)

