# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:09:00 2020

@author: abhij
"""
import numpy as np
import os

fname = os.path.join("aaaa.txt")
aaaatxt = np.loadtxt(fname,dtype=str)

fname1 = os.path.join("speffz.txt")
speffztxt = np.loadtxt(fname1,dtype=str)

        
#%%
res = list(set(aaaatxt)&set(speffztxt))
#%%
z = list(set(speffztxt) - set(res))
print(z)

#%%

res1 = list(set(z)^set(aaaatxt))

#%%
a=list(set(aaaatxt).intersection(z))
print(a)