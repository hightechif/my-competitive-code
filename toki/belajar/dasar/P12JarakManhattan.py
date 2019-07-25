# P12JarakManhattan.py : program utk menghitung jarak.
# Ridhan Fadhilah, 11-12-2015

n = list(map(int, input().split()))
jarak = abs(n[0]-n[2]) + abs(n[1]-n[3])
print(jarak)
