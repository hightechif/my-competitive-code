#belajar.py : Program untuk mempelajari suatu masukan.
#Ridhan Fadhilah, Sabtu 29 September 2018

# Fungsi untuk memberikan data
def data(x):
    return x

# Fungsi untuk mengecek suatu bilangna prima
def cekPrima(n):
    if n <= 1:
        return "bukan prima"
    elif n <= 3:
        return "prima"
    elif n % 2 == 0 or n % 3 == 0:
        return "bukan prima"
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "bukan prima"
        i += 6
    return "prima"

# Fungsi untuk mengecek jenis bilangan
def jenisbil(x,kotak):
    if x < 0:
        kotak.append("negatif")
    elif x == 0:
        kotak.append("nol")
    else:
        kotak.append("positif")
        if x % 2 != 0:
            kotak.append("ganjil")
            kotak.append(cekPrima(x))
        else:
            kotak.append("genap")
            kotak.append("bukan prima")
    return kotak

# Fungsi utama untuk mempelajari masukan
def belajar(x):
    import math
    hasil = []
    hasil.append(x)
    if type(x) == type(0):
        x = eval(x)
        hasil.append("integer")
        hasil = jenisbil(x,hasil)
    elif type(x) == type(0.0):
        x = eval(x)
        if math.floor(x)*1.0 == x:
            hasil.append("integer")
            hasil = jenisbil(x,hasil)
        else:
            hasil.append("fraction")
    elif type(x) == type(""):
        hasil.append("string")
    return hasil

masuk = eval(input())
materi = belajar(masuk)
print(materi)
