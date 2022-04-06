# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:10:57 2022

@author: Karsyn
"""

import pandas as pd

df = pd.read_csv('pct_distribution.csv')
        
df['% Sales Contribution']=round(df['Sales_dollar']/df['Sales_dollar'].sum()*100,2)
#print(df['% Sales Contribution'])

df.sort_values(by='% Sales Contribution', ascending= False, inplace=True)

df.reset_index(inplace=True, drop=True)

df['Sales_dollar'] = '$' + df['Sales_dollar'].astype(str)
df.rename(columns={'Sales_dollar': 'Sales'}, inplace=True)
print(df)