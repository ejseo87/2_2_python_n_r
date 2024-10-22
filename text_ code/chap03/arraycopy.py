import numpy as np # arraycopy.py

xm = np.array( [[1,2,3], [4,5,6], [7,8,9]] )
xm2 = xm
xm[0][0] = 10
print(xm)
print(xm2)

ym = np.array( [[1,2,3], [4,5,6], [7,8,9]] )
ym2 = ym.copy()
ym[0][0] = 10
print(ym)
print(ym2)

