# P23CekBilanganPrima.py : program utk mengecek suatu bilangan prima.
# Ridhan Fadhilah, 19-01-2016

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

for i in range(int(input())):
    q = cekPrima(int(input()))
    if q == True:
        print('YA')
    else:
        print('BUKAN')
