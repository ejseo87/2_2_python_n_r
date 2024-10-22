from copy import deepcopy # listcopy.py

xm = [[1,2,3], [4,5,6], [7,8,9]] 
# xm2 = xm 
xm2 = xm.copy()
xm[0][0] = 10
print(xm)
print(xm2)

ym = [[1,2,3], [4,5,6], [7,8,9]] 
# ym2 =deepcopy(ym)
ym2 = ym.copy()
ym[0][0] = 10
print(ym)
print(ym2)

ym = [[1,2,3], [4,5,6], [7,8,9]] 
ym2 = deepcopy(ym)
ym[0][0] = 10
print(ym)
print('ym2 width deep copy', ym2)

ym = [[1,2,3], [4,5,6], [7,8,9]] 
ym3 = ym[:][:]
ym[0][0] = 10
print(ym)
print('ym3 width slicing', ym3)


