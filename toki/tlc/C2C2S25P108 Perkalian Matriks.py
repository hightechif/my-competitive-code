# Matriks A
n = list(map(int, input().split()))
A, B, C, temp = ([],[],[],[])
for i in range(n[0]):
    a = list(map(int, input().split()))
    A.append(a)
# Matriks B
m = list(map(int, input().split()))
for i in range(m[0]):
    b = list(map(int, input().split()))
    B.append(b)
x,y,z = (n[0],m[0],m[1])
# Matriks C (B putar)
for i in range(z):
    for j in range(1,y+1):
        if j != y:
            temp.append(B[-j][i])
        else:
            temp.append(B[-j][i])
            C.append(temp)
            temp=[]
# Perhitungan Hasil    
hasil, wow = ([], 0)
for i in range(x):
    for k in range(z):
        for j in range(y):
            wow += A[i][j]*C[k][-(j+1)]
        hasil.append(wow)
        wow = 0
# Pencetakan Hasil
for t in range(len(hasil)):
    if (t+1) % z != 0:
        print(hasil[t], end=' ')
    else:
        print(hasil[t], end='\n')
