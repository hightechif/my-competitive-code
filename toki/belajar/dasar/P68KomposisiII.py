# P68KomposisiII.py : program utk menghitung nilai abs(Ax+B) dan di terapkan sebanyak K kali.
# Ridhan Fadhilah, 07-12 2018

masukan = input().split()
A = int(masukan[0])
B = int(masukan[1])
K = int(masukan[2])
x = int(masukan[3])

def F(x):
  res = abs(A*x+B)
  return res

for i in range(K):
  x = F(x)

print(x)
