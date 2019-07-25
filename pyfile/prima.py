# menentukan bilangan prima antara 1 sampai 1000
a = list(range(2,1000))
for i in a:
  for j in a:
    if j == i:
      continue
    elif j % i == 0:
      a.remove(j)

# mengambil bilangan prima diantara 100 sampai 1000
k = []
for v in a:
    if v > 100:
      k.append(v)

# mencetak 20 bilangan prima pertama yang lebih dari 100
for n in range(20):
  print(k[19-n]),
