a = []
n = int(input())
for i in range(n):
    e = int(input())
    a.append(e)
a.sort()
banyak = {}
for i in a:
    banyak[i] = banyak.get(i,0) + 1
v = max(banyak.values())
for j in a:
    if banyak[j] == v:
        k = j
print(k)
