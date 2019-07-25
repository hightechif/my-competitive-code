# P15While+Pencacah.py : program utk menjumlahkan semua input.
# Ridhan Fadhilah, 11-12-2015

j = 0
while True:
    try:
        j += int(input())
    except(EOFError): # ctrl + D
        break
print(j)
