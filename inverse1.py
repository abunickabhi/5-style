# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:09:00 2020

@author: abhij
"""
import numpy as np
import os


#%%
#text_file = open("C:\Users\abhij\Desktop\quads.txt", "r")
fname = os.path.join("quads1.txt")
str = np.loadtxt(fname,dtype=str)
str = np.delete(str, 0)

#%%
str = jan2021txt
new_words_list = [word[::-1] for word in str]

data = []
for i in str:
    if len(i) > 1 and i in new_words_list:
        data.append(i)
        
#%%
res = list(set(str)^set(data))
print(res)

#%%
res1=[]
for i in res:
    res1.append(i[::-1])
print(res1)