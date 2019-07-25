# bacaBerkas.py : Program Python untuk membuka dan membaca
#                 data suhu lingkungan pada suatu bulan.
# Agus Arif dkk, 07-10-2015

# Buka Berkas
namaBerkas = 'suhu_mei.txt'
berkas = open(namaBerkas, mode='r')

# Membaca baris-baris data dari berkas
jumlah = 0
N = 0
for i in berkas:
  data = int(i)
  jumlah += data
  N += 1
  print N, data, jumlah

# Menutup berkas
berkas.close()

# Menghitung rerata suhu dalam 1 bulan
meanSuhu = float(jumlah) / N
print 'Suhu rerata sebanyak %d data adalah %.2f' % (N, meanSuhu)
