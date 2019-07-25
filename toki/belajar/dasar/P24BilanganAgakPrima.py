# P24BilanganAgakPrima.py : program utk mengecek suatu bilangan agak prima.
# Ridhan Fadhilah, 03-02-2016

def AP(x):
    bts = int(x**0.5)
    count = 0
    for i in range(2,bts+1):
        if x % i == 0:
            count += 1
            if count > 1:
                return False
    return True

n = int(input())
for i in range(n):
    if AP(int(input())):
        print('YA')
    else:
        print('BUKAN')
