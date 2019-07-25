# P5LuasSegitia.py : program utk menghitung luas segitiga.
# Ridhan Fadhilah, 10-12-2015

a,b  = map(float, input().split()) # masukan alas dan tinggi
luas = (a*b)/2                     # formula mencari luas segitiga
print ('%.2f' % luas)              # menampilkan hasil 2 dibelakang koma
