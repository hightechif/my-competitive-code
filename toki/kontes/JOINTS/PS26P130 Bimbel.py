n = list(map(int, input().split()))
N, M = (n[0],n[1])
hasil = N+1-int((N+1)/M)
if (N+1) % M == 0:
    hasil += 1
print(hasil)
