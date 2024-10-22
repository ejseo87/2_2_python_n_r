# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:05:55 2019

@author: Sim
"""

import re

mystr = re.sub('\\[', 'A',  '[12.5+13-1*5$')
print(mystr)

mystr = re.sub('[a-z]', '-',  'bcde0123ABC')
print(mystr)

l_case = re.search('[a-z]', 'bcde0123ABC')
if l_case: print('a-z exits')
else: print('No a-z')

l_case = re.search('[k-z]', 'bcde0123ABC')
if l_case: print('k-z exists')
else: print('No k-z')


mystr =  [re.sub('grey|gray', 'GRAY',  word) for word in 
     ['grey', 'gray', 'groy', 'greay', 'greey']]
print(mystr)

mystr=[re.sub('gr(a|e)y', 'GRAY', word) for word in
       ['grey', 'gray', 'groy', 'greay', 'greey']]
print(mystr)



