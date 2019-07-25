# Bagian Input & Inisiasi
x,y,z = list(map(int, input().split()))
C,temp,hasil,wow = ([],[],[],0)

# Matriks A
A = [list(map(int, input().split())) for i in range(x)]

# Matriks B
B = [list(map(int, input().split())) for i in range(y)]

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
