# faktorial : Program untuk menghitung nilai faktorial.
# Ridhan Fadhilah, 01-04-2018

def fakt(x):
    res = 1
    if x%2 == 0:
        for i in range(1,x//2+1):
            res = res*i*(x+1-i)
    else:
        x = x+1
        for i in range(1,x//2+1):
            res = res*i*(x+1-i)
        res = res//x
    return res

n = int(input())
for i in range(n+1):
    print(i,fakt(i))
#print(fakt(75))
