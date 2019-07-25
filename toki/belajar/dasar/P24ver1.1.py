# P24BilanganAgakPrima.py : program utk mengecek suatu bilangan agak prima.
# Ridhan Fadhilah, 19-01-2016

import math
c = int(input())
for a in range(c):
    pr = int(input())
    cek = 0
    tes = 3
    bts = int(pr**0.5)
    if ( pr % 2 == 0 & pr != 2 ) or pr == 1:
        cek += 1
    while tes <= bts:
        if pr % tes == 0:
            cek += 1
            if cek > 2:
                break
        tes += 1
    if cek > 2:
        print('BUKAN')
    else:
        print('YA')
