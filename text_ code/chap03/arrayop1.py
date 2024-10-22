import numpy as np  # arrayop1.py

a = np.array(range(1,11,2))
a1 = np.delete(a, 2)
idx = [0, 1,3]
a2 = np.delete(a, idx)

b1= 11
a3 = np.append(a, b1)
b2 = 2
a4 = np.insert(a, 1, b2)
b3 = [1,2,3]
a5 = np.insert(a, 2, b3)

mx1 = np.array(range(1,10)).reshape(3,3)

mx2 = np.append(mx1, np.array([10, 20, 30]).reshape(1,3), axis=0)
mx3 = np.append(mx1, np.array([10, 20, 30]).reshape(3,1), axis=1)

mx4 = np.delete(mx1, 0, axis=0) # 첫째행 삭제
mx5 = np.delete(mx1, [0,1], axis=1) # 1, 2열 삭제

mx6 = np.insert(mx1, 1, np.array([10, 20, 30]), axis=0)
mx7 = np.insert(mx1, 1, np.array(range(10, 100, 10)).reshape(3,3), axis=1)

r1 = np.array([1,2,3]) ; r2 = np.array([4,5,6]); r3 = np.array([7,8,9])
vx1 = np.hstack( (r1, r2, r3) )
mx8 = np.vstack( (r1, r2, r3) )

c1 = np.array([[1],[2],[3]]) 
c2 = np.array([[4],[5],[6]])
c3 = np.array([[7],[8],[9]])
mx9 = np.hstack( (c1, c2, c3) )
mx10 = np.vstack( (c1, c2, c3) )
