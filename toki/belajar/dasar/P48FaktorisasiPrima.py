def cekPrima(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

v = int(input())
bil = list(i for i in range(2,int(v**0.5)))
for i in bil:
    for j in bil:
        if i == j:
            continue
        elif j % i == 0 or v % j != 0:
            bil.remove(j)
n=v
px=1
banyak = {}
output = ''

if cekPrima(v)==True:
    print(v)
else:
    for i in bil:
        while n%i==0:
            px*=i
            n/=i
            banyak[i] = banyak.get(i,0) + 1
    f = int(v/px)
    if cekPrima(f)==True:
            banyak[f] = 1
    b = list(banyak.keys())
    b.sort()
    for i in range(len(b)):
        if i == len(b)-1:
            if banyak[b[i]]!=1:
                output += str(b[i])+'^'+str(banyak[b[i]])
            else:
                output += str(b[i])
        else:
            if banyak[b[i]]!=1:
                output += str(b[i])+'^'+str(banyak[b[i]])+' x '
            else:
                output += str(b[i])+' x '
    print(output)
