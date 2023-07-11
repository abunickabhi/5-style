"""
Created on Sun Feb 7 05:01:05 2021

@author: abhi

This is a working code that takes one alg sequences and makes it into Yo notation. Work is still going on to make it function for batches.
"""
import re
import pyperclip
string = input("Enter the alg:")
string = string + " "

string = re.sub(r'(M )(?!\')', 'm', string)
string = re.sub(r'(M\' )(?!\')', 'n', string)
string = re.sub(r'(M2 )(?!\')', 'o', string)
string = re.sub(r'(U )(?!\')', 'a', string)
string = re.sub(r'(U\' )(?!\')', 'b', string)
string = re.sub(r'(U\' )(?!\')', 'b', string)
string = re.sub(r'(U2 )(?!\')', 'c', string)
string = re.sub(r'(L )(?!\')', 'g', string)
string = re.sub(r'(L\' )(?!\')', 'h', string)
string = re.sub(r'(L2 )(?!\')', 'i', string)
string = re.sub(r'(R )(?!\')', 'j', string)
string = re.sub(r'(R\' )(?!\')', 'k', string)
string = re.sub(r'(R2 )(?!\')', 'l', string)
string = re.sub(r'(F )(?!\')', 'v', string)
string = re.sub(r'(F\' )(?!\')', 'w', string)
string = re.sub(r'(F2 )(?!\')', 'x', string)
string = re.sub(r'(D )(?!\')', 'd', string)
string = re.sub(r'(D\' )(?!\')', 'e', string)
string = re.sub(r'(D2 )(?!\')', 'f', string)
string = re.sub(r'(E )(?!\')', 'p', string)
string = re.sub(r'(E\' )(?!\')', 'q', string)
string = re.sub(r'(E2 )(?!\')', 'r', string)
string = re.sub(r'(S )(?!\')', 's', string)
string = re.sub(r'(S\' )(?!\')', 't', string)
string = re.sub(r'(S2 )(?!\')', 'u', string)
string = re.sub(r'(u )(?!\')', 'qa', string)
string = re.sub(r'(u\' )(?!\')', 'bp', string)
string = re.sub(r'(u2 )(?!\')', 'rc', string)
string = re.sub(r'(r )(?!\')', 'nj', string)
string = re.sub(r'(r\' )(?!\')', 'mk', string)
string = re.sub(r'(r2 )(?!\')', 'ol', string)
string = re.sub(r'(l )(?!\')', 'mg', string)
string = re.sub(r'(l\' )(?!\')', 'nh', string)
string = re.sub(r'(l2 )(?!\')', 'oi', string)
string = re.sub(r'(f )(?!\')', 'sv', string)
string = re.sub(r'(f\' )(?!\')', 'wt', string)
string = re.sub(r'(f2 )(?!\')', 'xu', string)
string = re.sub(r'(d )(?!\')', 'pd', string)
string = re.sub(r'(d\' )(?!\')', 'eq', string)
string = re.sub(r'(d2 )(?!\')', 'rf', string)
string = ' '.join(re.findall(r'.{1,4}', string))

#print(string)
pyperclip.copy(string)

#%%
f=\
lambda a:[(v+"'")[:2-("'"in v)]for v in a[::-1]]
string = input("Enter the alg:").split()
output = f(string)
output = ' '.join(map(str, output))
pyperclip.copy(output)