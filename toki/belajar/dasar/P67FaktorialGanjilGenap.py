# P67FaktorialGanjilGenap.py : program utk menghitung faktorial dengan aturan ganjil genap.
# Ridhan Fadhilah, 07-12 2018

def faktorial(x):
  y = oddeven(x)
  if y == 0:
    return 1
  else:
    return y*faktorial(x-1)

def oddeven(x):
  if x % 2 == 0:
    return x//2
  else:
    return x

x = int(input())
print(faktorial(x))
