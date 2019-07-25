def swap(a,b,daftar):
    idxa = daftar.index(a)
    idxb = daftar.index(b)
    daftar[idxa] = b
    daftar[idxb] = a
    return daftar

l = []
nilai = []
n = int(input())
h = [""]*n
for a in range(n):
    x = input()
    l.append(x)
    nilai.append(len(x))
    
while True:
    x1 = l[0]
    for i in range(1,len(l)):
        x2 = l[i]
        if len(x1) > len(x2):
            h[l.index(x1)] = x2
            h[l.index(x2)] = x1
        else:
            h[l.index(x1)] = x1
            h[l.index(x2)] = x2
        x1 = x2
    if (len(h[0]) != min(nilai) & len(h[n-1]) != max(nilai)):
        break
