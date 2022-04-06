# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:09:07 2022

@author: Karsyn
"""

import numpy as np 
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import statsmodels.formula.api as smf
import statsmodels.api as sm


df = pd.read_csv('sacramento.csv')

#df = df.loc[df['type'] != 'Condo']

df['baths'] = df['baths'].astype(float)
df['beds'] = df['beds'].astype(float)
df['sqft'] = df['sqft'].astype(float)
df['price'] = df['price'].astype(float)

df['num_bath'] = np.select([(df['baths']==1), df['baths']>1],[0,1])

#print(df['num_bath'].head(20))
x=df.loc[:,['beds','sqft', 'price']]
y=df['num_bath']
tot=sm.add_constant(x, prepend=True)


mod=sm.Logit(y, tot).fit()
mod.summary()


print(mod.params.round(2))
print(mod.pvalues.round(2))
print('The smallest p-value is for sqft')


