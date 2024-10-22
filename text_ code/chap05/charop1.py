# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:25:12 2019

@author: hallym
"""

a = "abc"
print(len(a))
print(a[1])

x,y,z = a

print(x)

aa = a +"ABC"
print(aa)
aaa = a * 3
print(aaa)

bb = 'A test string'
blist0 = bb.split()
blist1 = bb.split('i')
print(blist0, blist1)

mystr = 'abcdeabcab'
n0 = mystr.count('ab')
n1 = mystr.find('ab')
n2 = mystr.rfind('ab')
newstr = mystr.replace('ab', 'AB')
print(n0, n1, n2, newstr)