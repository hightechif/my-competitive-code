def gv(x,y):
    if x == -1 or x == n or y == -1 or y == m:
        return 1
    return h[x][y]
n,m,k = map(int, input().split())
h = [list(map(int, input().split())) for i in range(n)]
o = (0,0)
for j in range(m):
    if o != (0,0):
        break
    for i in range(n):
        if k == gv(i-1,j) * gv(i+1,j) * gv(i,j-1) * gv(i,j+1):
            o = (i+1, j+1)
            break
print('{} {}'.format(o[0],o[1]))
