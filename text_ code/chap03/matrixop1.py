import numpy as np # matrixop1.py

mtx = np.array([[1,2,3], [4,5,6]])
mtx = np.array([1,2,3,4,5,6]).reshape(2,3)

mx1 = np.array(range(1,7)).reshape(2,3)
mx2 = np.hstack((np.repeat(1,3).reshape(3,1), np.repeat(2,3).reshape(3,1)))
mx3 = np.matmul(mx1, mx2)
print(mx3.shape)

# example of hstack

a = np.array([1,2,3])
b = np.array([2,3,4])
a + b
Out[36]: array([3, 5, 7])
np.hstack([a,b])
Out[38]: array([1, 2, 3, 2, 3, 4])

mx3
Out[52]: 
array([[ 6, 12],
       [15, 30]])

# Example of transpose and Inverse matrix

mx = np.array([1,2,3,4]).reshape(2,2)

mx
Out[63]: 
array([[1, 2],
       [3, 4]])

mx.transpose()
Out[68]: 
array([[1, 3],
       [2, 4]])

imx = np.linalg.inv(mx)
imx
Out[65]: 
array([[-2. ,  1. ],
       [ 1.5, -0.5]])

np.matmul(mx, imx)
Out[66]: 
array([[1.00000000e+00, 1.11022302e-16],
       [0.00000000e+00, 1.00000000e+00]])
