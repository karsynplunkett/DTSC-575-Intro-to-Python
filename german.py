# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:58:29 2022

@author: Karsyn
"""

#import numpy as np 
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import statsmodels.formula.api as smf
import statsmodels.api as sm

df = pd.read_csv('german_credit_data.csv')

df.rename(columns={'Credit amount': 'Credit_amount'}, inplace=True)


y = df[['Age','Duration']]
x=df['Credit_amount']
#sns.scatterplot(data=ff, x=x, y=y)
total_constant=sm.add_constant(y, prepend=True)

mod1=sm.OLS(x,total_constant)
model=mod1.fit()

print(model.params.round(2))
print(model.rsquared.round(2))
