import random

sudah=[]
banyak = 0
while banyak < 17:
    x=random.randint(97,113)
    if x not in sudah:
        sudah.append(x)
        print(chr(x))
        banyak += 1
    else:
        continue
    
