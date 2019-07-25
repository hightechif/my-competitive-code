# P19PolaI.py : program utk menghasilkan pola I.
# Ridhan Fadhilah, 27-12-2015

a,b = map(int,input().split())
k = ''
for i in range(1,a+1):
    if i % b == 0:
        k += '*'
    else:
        k += str(i)
    if i < a:
        k += ' '
print(k)
