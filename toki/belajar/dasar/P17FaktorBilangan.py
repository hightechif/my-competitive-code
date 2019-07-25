# P17FaktorBilangan.py : program utk menentukan faktor bilangan.
# Ridhan Fadhilah, 13-12-2015

n = int(input())
for i in range(n,0,-1):
    if n % i == 0:
        print(i)
