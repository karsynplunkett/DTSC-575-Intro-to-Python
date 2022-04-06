# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:56:35 2022

@author: Karsyn
"""

import sys
import pandas as pd
import numpy as np

def randdf(x,y):
        x=int(x)
        y=int(y)
        rng=np.random.RandomState(56)
        df=pd.DataFrame(rng.randint(0,100,(x,y)))
        print(df)
  
#randdf(3,6)       
randdf(sys.argv[1],sys.argv[2])