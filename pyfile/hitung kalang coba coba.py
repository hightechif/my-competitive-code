daftar = {'a':{'x':1,'y':2,'z':3},'b':{'x':4,'y':5,'z':6},'c':{'x':7,'y':8,'z':9}}
print(daftar.values())
print()
print(daftar.keys())
print()
print()
for i,a in daftar.items():
    print(i,end=' ')
    for j in a.keys():
        print(str(a[j]),end=' ')
    print()
