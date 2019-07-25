# P22PolaIII.py : program utk menghasilkan pola III.
# Ridhan Fadhilah, 27-12-2015

n = int(input())
k = 0
for i in range(1,n+1):
    for j in range(i):
        if k > 9:
            k = 0
        print(k, end='')
        k += 1
    print()
