# P16DuaPangkat.py : program utk mengecek bilangan 2 pangkat.
# Ridhan Fadhilah, 11-12-2015

n = int(input())
if n != 1:
    while n > 2:
        n /= 2
    if n == 2:
        print('ya')
    else:
        print('bukan')
else:
    print('ya')
