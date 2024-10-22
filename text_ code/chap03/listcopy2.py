# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:54:57 2019

@author: Sim
"""

xv = [1,2,3]
xv2 = xv
xv3 = xv.copy()

xv.append("added item")
print("xv = ", xv, "\nxv2 = ", xv2, "\nxv3 = ", xv3)