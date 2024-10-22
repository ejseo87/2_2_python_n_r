# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:37:09 2019

@author: hallym
"""

x = range(1,6)
for j in x:   
# if (j == 3): continue
 print(j, " ")
else: 
 print("정상적인 반복종료")
 
x = range(1,6)
for j in x:   
 if (j == 3): break
 print(j, " ")
else: 
 print("정상적인 반복종료") 