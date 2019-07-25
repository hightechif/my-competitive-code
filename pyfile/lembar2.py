uang = [100,50,20,10,5,1]
cacah = [0,0,0,0,0,0]
def lembar(x):
    for i in range(6):
        cacah[i] = x//uang[i]
        x = x % uang[i]
    return cacah
n = int(input())
hasil = lembar(n)
for j in range(6):
    print(uang[j],":",hasil[j])
