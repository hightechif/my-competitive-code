# KaplanTurbine.py: program utk menghitung dan menampilkan kalkulasi Turbin Kaplan.
# Ridhan Fadhilah, 26 September 2018

print("Program Perhitungan untuk Turbin Kaplan")
print("---------------------------------------")
print()
data = eval(input("Banyak data = "))
print()
for i in range(data):
    print("Data ke",i)
    print("Masukan nilai yang dibutuhkan:")
    
    H = float(input("Masukan nilai ketinggian (H) = "))
    Q = float(input("Masukan nilai debit (Q) = "))
    n = float(input("Masukan nilai Rotasi Turbin (n) = "))

    #Tetapan, Konstanta dan Koefisien
    g = 9.81     # percepatan gravitasi
    Cv = 0.97    # Coefficient Factor
    rho = 1000   # Densitas air
    ethag = 0.85 # Efisiensi Generator
    etham = 0.90 # Efisiensi Mekanis

    #1 Kecepatan Aliran Fluida (V1) yang dialirkan ke Turbin
    V1 = ((2*g*H)**0.5)*Cv

    #2 kecepatan Putar OMEGA (OM)
    OM = n*0.104

    #3 Mencari Fungsi (Aa)
    Aa = OM/V1

    #4 Mencari Fungsi (Am)
    Am = Q/V1

    #5 Mencari Fungsi (Qn)
    Qn = Aa*(Am**0.5)
    
    #6 Mencari Fungsi (C)
    C = 0.12 + (0.18*Qn)
    
    #7 Mencari Diameter (D)
    D = (Am*4/(3.14*C))

    #8 Mencari Daya (P) Listrik yang mungkin di hasilkan (Daya Bersih ke turbin)
    P = Q*H*g*rho*ethag*etham

    #9 Mencari (Ns)
    Ns = n*(P**0.5)/(H**1.25)

    print()
    print("Hasil Kalkulasi untuk Turbin Pelton")
    print("-----------------------------------")
    print("P       = %.3f" % P)
    print("D       = %.3f" % D)
    print("Ns      = %.3f" % Ns)
    print()
    print()
