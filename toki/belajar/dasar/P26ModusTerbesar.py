# P26ModusTerbesar.py : program utk menentukan nilai modus terbesar.
# Ridhan Fadhilah, 03-02-2016

input()
a = list(map(int, input().split()))
a.sort()
a = a[::-1]
banyak = {}
for i in a:
    banyak[i] = banyak.get(i,0) + 1
v = max(banyak.values())
for j in a:
    if banyak[j] == v:
        res = j
        break
print(res)
