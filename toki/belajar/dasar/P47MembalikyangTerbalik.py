def balik(x):
    h=''
    while x[-1] == '0':
        x = x[:len(x)-1]
    for i in range(1,len(x)+1):
        h += x[-i]
    return h
a,b = input().split()
newa=int(balik(a))
newb=int(balik(b))
hasil=str(newa+newb)
print(balik(hasil))
