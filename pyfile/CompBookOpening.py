hasil = 1000
coor = []
n = int(input())
if n >= 1: x0,y0 = map(int, input().split())
for i in range(2*n-1):
    x,y = map(int, input().split())
    coor.append([x,y])
for x,y in coor:
    hasil = min(((x-x0)**2 + (y-y0)**2)**0.5,hasil)
    x0 = x
    y0 = y
print(hasil)
