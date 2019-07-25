n = list(map(int, input().split()))
x, y = (n[0],n[1])

k = []
for i in range(x):
    a = list(map(int, input().split()))
    k.append(a)

for i in range(y):
    for j in range(1,x+1):
        if j != x:
            print(k[-j][i], end=' ')
        else:
            print(k[-j][i], end='\n')
