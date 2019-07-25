buku = {}
n,q = map(int, input().strip().split())
for i in range(n):
    nama,no = input().strip().split()
    buku[nama] = no
for i in range(q):
    nama = input()
    if nama in buku.keys():
        print(buku[nama])
    else:
        print("NIHIL")
