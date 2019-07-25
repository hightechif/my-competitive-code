# P70KonversiBiner.py : program utk mengkonversi bil decimal ke biner.
# Ridhan Fadhilah, 07-12 2018

num = int(input())
hasil = ''
if num == 0:
  hasil = num
while num > 0:
  if num % 2 == 0:
    hasil = '0' + hasil
  else:
    hasil = '1' + hasil
  num = num//2
print(int(hasil))
