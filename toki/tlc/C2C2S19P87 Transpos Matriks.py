k = []
for i in range(3):
    a = list(map(int, input().split()))
    k += a
for j in range(3):
    print(k[j],k[j+3],k[j+6])
