# segitiga.py : Program Python untuk mencari luas segitiga sembarang setelah
#               panjang sisi - sisinya diberikan melalui papan-ketik.

# Kelompok 1 Teknik Fisika C 2015
# Anggota Kelompok:
#                  Aan Listanto     44091
#                  M. Gozha A.      43511
#                  Najmi Jamal      43516
#                  R. M. Faisal     43519
#                  Ridhan Fadhilah  43521
#                  Yetri Tanoen     44116
#                                                                 23-09-2015


# Judul Program
print ' ' * 5 + 'Menghitung Luas Segitiga Sembarang dari Nilai Panjang Sisi - sisinya.'
print ' ' * 5 + '--------------------------------------------------------------------\n'

# Sambutan
print ' ' * 25 + 'Selamat datang di program kami\n'

# Pemberian sisi - sisi segitiga
a = raw_input('Masukan panjang sisi a = ')
a = abs(float(a))
b = raw_input('Masukan panjang sisi b = ')
b = abs(float(b))
c = raw_input('Masukan panjang sisi c = ')
c = abs(float(c))
print 'Panjang sisi - sisinya: ', a, b, c

# Hitung semiperimeter
s = (a + b + c)/2
print 'Nilai semiperimeter (s) = ', s

# Hitung luas segitiga
L = (s * (s-a) * (s-b) * (s-c)) ** 0.5

# Tampilkan nilai luas segitiga
print 'Luas segitiga = ', L

# Ucapan Terima Kasih
print '\n' + ' ' * 18 + 'Terima kasih telah menggunakan program kami.'
