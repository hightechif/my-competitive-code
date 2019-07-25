# P25BalikDaftar.py : program utk membalik suatu daftar.
# Ridhan Fadhilah, 03-02-2016

c = []
while True:
    try:
        c.insert(0,str(input()))
    except EOFError:
        break
print('\n'.join(c))
