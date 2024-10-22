# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:03:16 2020

@author: Sim
"""

import datetime as dt

now = dt.datetime.now()

print(now.year, now.month, now.day, 
      now.hour, now.minute, now.second)
print(now.strftime("%Y-%m-%d: %A")) 

dob1 = dt.datetime(2000, 5, 17)
age = now.year - dob1.year
print("나이 =", age)

