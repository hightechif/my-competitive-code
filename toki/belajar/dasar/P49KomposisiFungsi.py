def f(x):
    global a,b
    h = abs(a*x+b)
    return h

a,b,k,x = map(int,input().split())
h = f(x)
for i in range(k-1):
        h = f(h)
print(h)
