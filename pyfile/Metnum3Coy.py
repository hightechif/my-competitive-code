import math
h = 2.2
a = [ float(('%.2f') % (8+(h*i))) for i in range(11)]
hasil = []
def f(t):
    f = 2000*(math.log10(140000/(140000-2100*t))/math.log10(math.e))-9.8*t
    return f
print(math.log10((math.e)**math.e)/math.log10(math.e))
print()
for i in a:
    hasil.append(float(('%.2f') % (f(i))))
for i in range(len(hasil)):
    print(a[i],hasil[i])
print()
p = 2*(sum(hasil)-hasil[0]-hasil[-1])
x = h/2*(hasil[0]+p+hasil[-1])
print(h/2,p)
print(x)
