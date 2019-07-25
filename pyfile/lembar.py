uang = [100,50,20,10,5,1]
cacah = [0,0,0,0,0,0]
def lembar(x):
    for i in range(6):
        while x >= uang[i]:
            cacah[i] += 1
            x -= uang[i]
    return cacah
n = int(input())
hasil = lembar(n)
for j in range(6):
    print(uang[j],":",hasil[j])
