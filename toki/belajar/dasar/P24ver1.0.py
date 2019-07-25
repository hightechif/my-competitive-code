# P24BilanganAgakPrima.py : program utk mengecek suatu bilangan agak prima.
# Ridhan Fadhilah, 19-01-2016

def ap(n):
    y = 1
    if n == 1:
        y = 1
    else:
        for i in range(2,n+1):
            if n % i == 0:
                y += 1
    if y <= 4:
        return True
    else:
        return False

banyak = int(input())
r = []
for i in range(banyak):
    x = int(input())
    r.append(x)

for i in range(banyak):
    b = ap(r[i])
    if b == True:
        print('YA')
    else:
        print('BUKAN')
