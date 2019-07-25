kata = input()
kunci = input()

# Bentuk 1
a = 0
hitung = 0
for i in range(len(kunci)):
    for j in range(a,len(kata)):
        if kata[j] == kunci[i]:
            a = j+1
            hitung +=1
            break
if hitung == len(kunci):
    print('Ada')
else:
    print('Tidak ada')

# Bentuk 2
def bforce(x,t,h=0):
    while x != '':
        y = t
        if x[0] == y[0]:
            y = y[1:]
            x = x[1:len(y)+1]
            h += 1
            return bforce(x,y)
        else:
            x = x[1:]
            return bforce(x,y)
    return True if h == len(t) else False

print(bforce(kata,kunci))

# Bentuk 3
def w(x,y):
    x = [i for i in x]
    x.append(y)
    i = 0
    while x[i] != y:
        i += 1
    return i if i<len(x) else -1

print(w(kata,kunci))
