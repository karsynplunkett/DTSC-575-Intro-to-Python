# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:05:30 2022

@author: Karsyn
"""

import pandas as pd

df = pd.read_csv('groupby_practice.csv')

#df['Sales_dollar_product']=df.groupby(['Product']).sum()
df.groupby('Product').agg({'Sales_dollar':'sum'}).rename({'Sales_dollar':'Sales_dollar_product'}, axis=1)
df.groupby('Sold_by').agg({'Sales_dollar':'sum'}).rename({'Sales_dollar':'Sales_dollar_person_product'}, axis=1)

df_dummy = df[df['Sales_dollar'] < 50]
#1 level
df_dummy.groupby('Sold_by').agg({'Sales_dollar':'sum'}).rename({'Sales_dollar':'Sales_dollar_person'}, axis=1)

#2 levels
df_dummy.groupby(['Sold_by', 'Product']).agg({'Sales_dollar':'sum'}).rename({'Sales_dollar':'Sales_dollar_person_product'}, axis=1)

print(df)