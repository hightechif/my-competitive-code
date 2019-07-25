# putar

import numpy as np
def putar(y):
    a = y[1,0]
    b = y[0,0]
    c = y[1,1]
    d = y[0,1]
    z = np.array([[a,b],[c,d]])
    return z
def putarn(x,n):
  for i in range(n):
    x = putar(x)
  return x

e = np.array([[5,6],
              [7,8]])
v = int(raw_input())
h = putarn(e,v)
print h
