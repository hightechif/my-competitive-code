def binarySearch(h,x):
    h.sort()
    hasil = 0
    kiri = 1
    kanan = len(h)
    while kiri <= kanan and hasil == 0:
        tengah = (kiri + kanan)//2

        if x < h[tengah]:
            kanan = tengah - 1
        elif x > h[tengah]:
            kiri = tengah + 1
        else:
            hasil = tengah
    return hasil

angka = [i for i in range(34,10002)]
index = binarySearch(angka,55)
print(angka)
print(index, angka[index])
