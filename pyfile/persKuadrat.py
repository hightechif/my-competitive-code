# persKuadrat.py : Program Python untuk mencari 2 akar persamaan kuadrat
#                  setelah 3 koefisiennya diberikan melalui papan-ketik.
# Ridhan Fadhilah, 23-09-2015

# Ulangi Kala 
jawab = 'Y'
while jawab == 'Y':
  # Berikan 3 Koefisien A, B, C
  A = input('\nKoefisien A = ')
  A = float(A)
  B = input('Koefisien B = ')
  B = float(B)
  C = input('Koefisien C = ')
  C = float(C)
  print('Koefisien persamaan kuadrat:' , A, B, C)

  # Hitung Diskriminan
  D = B ** 2 - 4 * A * C
  print('Diskriminan =', D)

  # Tentukan jenis akar dan hitung nilainya
  if D > 0:
    print('Akar yang real dan berbeda')
    x1 = (-B + D ** 0.5) / (2 * A)
    x2 = (-B - D ** 0.5) / (2 * A)
  elif D == 0:
    print('Akar yang real dan kembar')
    x1 = -B/(2 * A)
    x2 = x1
  else:
    print('Akar yang kompleks')
    x1 = (-B)/(2 * A) + (1j * abs(D) ** 0.5) / (2 * A)
    x2 = (-B)/(2 * A) - (1j * abs(D) ** 0.5) / (2 * A)

  # Tampilkan 2 akar persamaan kuadrat
  print('Akar persamaan kuadrat =', x1, x2)

  # Uji apakah ingin mengulang program
  jawab = input('Ulangi (Y/T) ? ')
