# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:54:56 2022

@author: Karsyn
"""

#import numpy as np 
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import statsmodels.formula.api as smf
import statsmodels.api as sm

ff = pd.read_csv('fastfood.csv')


y = ff[['total_fat','sat_fat','cholesterol','sodium']]
x=ff['calories']
#sns.scatterplot(data=ff, x=x, y=y)
total_constant=sm.add_constant(y, prepend=True)

mod1=sm.OLS(x,total_constant)
model=mod1.fit()

print(model.mse_total.round(2))
print(model.rsquared.round(2))
print(model.params.round(2))
print(model.pvalues.round(2))

