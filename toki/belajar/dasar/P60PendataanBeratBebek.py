import bisect 
n = int(input())
datan = list(map(int, input().split()))
for i in range(int(input())):
    x,y = map(int, input().split())
    hasil = bisect.bisect(datan, y) - bisect.bisect(datan, x)
    print(hasil)
