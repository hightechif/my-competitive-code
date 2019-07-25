# P21PolaII.py : program utk menghasilkan pola II.
# Ridhan Fadhilah, 27-12-2015

n = int(input())
for i in range(1,n+1):
    print((n-i)*' ' + i*'*')
