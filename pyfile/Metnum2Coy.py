import math

h = 2.2
a = [ float(('%.2f') % (8+((h/2)*(2*i+1)))) for i in range(11)]
a.sort()
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

p = sum(hasil)-hasil[-1]
x = h*p
print(h,p)
print(x)
