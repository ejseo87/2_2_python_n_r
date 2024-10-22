# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:04:26 2020

@author: Sim
"""

import datetime as dt

def birthyear():
  age = input("Enter age: ")
  now = dt.datetime.now()
  curyear = now.year
  b_year = curyear-int(age)
  print("born.year= ", b_year)

birthyear()
