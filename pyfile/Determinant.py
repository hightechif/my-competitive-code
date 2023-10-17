import numpy as np

# Determinant
def det2(x):
  j = x[0,0]*x[1,1] - x[0,1]*x[1,0]
  return j
def det3(y):
  k = y[0,0]*det2(y[1:,1:])-y[0,1]*det2(y[1:,::2])+y[0,2]*det2(y[1:,:2])
  return k

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
n = np.array([[1,0,0],
              [5,1,0],
              [17,8,1]])
o = np.array([[2,0,1],
              [5,1,0],
              [17,8,1]])
print(det3(a))
print(np.linalg.det(a))
print(det3(n))
print(np.linalg.det(n))
print(det3(o))
print(np.linalg.det(o))
