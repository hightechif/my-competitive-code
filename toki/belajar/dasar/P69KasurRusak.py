# P69KasurRusak.py : program utk klasifikasi kata palindrom.
# Ridhan Fadhilah, 07-12 2018

x = input()
if x == x[::-1]:
    print("YA")
else:
    print("BUKAN")
