# P13For(KandangBebek).py : program utk menghitung banyaknya total bebek.
# Ridhan Fadhilah, 11-12-2015

n   = int(input())
b   = input().split()
res = 0
for i in range(n):
    res += int(b[i])
print(res)
