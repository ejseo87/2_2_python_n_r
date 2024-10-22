# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:06:43 2019

@author: root
"""

from pandas import DataFrame

cars = {'make': ['Hyundai','Kia','Ford','Chevrolet'],
        'model': ['Sonata', 'K5', 'Taurus', 'Impala'],
        'price':  [3200,3100,3500,3700]         }

df = DataFrame(cars)
write_txt = df.to_csv (r'E:\hwp\books\pr4ds\cars.txt',  sep = " ", 
                        index = True, header=True) 

f=open("E:/hwp/books/pr4ds/cars.csv","w")
write_csv = df.to_csv (f,  sep = ",", index = None, header=True) 
f.close()
print (df)


