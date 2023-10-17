# PeltonTurbine.py: program utk menghitung dan menampilkan kalkulasi Turbin Pelton.
# Ridhan Fadhilah, 22 September 2018

print("Program Perhitungan untuk Turbin Pelton")
print("---------------------------------------")
print()
print("Masukan nilai yang dibutuhkan:")

H = float(input("Masukan nilai ketinggian (H) = "))
Q = float(input("Masukan nilai debit (Q) = "))

#Tetapan, Konstanta dan Koefisien
g = 9.81     # percepatan gravitasi
Cv = 0.97    # Coefficient Factor
rho = 1000   # Densitas air
ethag = 0.85 # Efisiensi Generator
etham = 0.90 # Efisiensi Mekanis

#1 Kecepatan Aliran Fluida (V1) yang dialirkan ke Turbin
V1 = ((2*g*H)**0.5)*Cv

#2 Kecepatan Bucket pada Turbin (U)
U = 0.45*V1

#3 Mencari Fungsi Euler (E) Head Loss karena Friksi
E = (U*(V1-U)*1.821)/g

#4 Nozzle Dimensions (An)
An = Q/V1

#5 Nozzle Diameter (Dn)
Dn = (An*1.274)**0.5

#6 Diameter of Pleton Wheel (Drun)
Drun = (60*U)/1884

#7 Jumlah Buckets (Bn)~
Bn = (0.5*Drun/Dn)+15

#8 Dimensions of Bucket
B = 4*Dn
D = 0.9*Dn
M = 1.1*Dn
L = 2.4*Dn

#9 Mencari Daya (P) Listrik yang mungkin di hasilkan (Daya Bersih ke turbin)
P = Q*E*g*rho*ethag*etham

print()
print("Hasil Kalkulasi untuk Turbin Pelton")
print("-----------------------------------")
print("V1      = %.3f" % V1)
print("U       = %.3f" % U)
print("E       = %.3f" % E)
print("P       = %.3f" % P)
print("Anozzle = %.6f" % An)
print("Dnozzle = %.3f" % Dn)
print("Dturbin = %.3f" % Drun)
print("Bilah   = %.3f" % Bn)
print("B       = %.3f" % B)
print("D       = %.3f" % D)
print("M       = %.3f" % M)
print("L       = %.3f" % L)
