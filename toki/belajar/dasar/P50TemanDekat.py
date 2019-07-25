n,d = map(int, input().split())
x,y,h = ([],[],[])
for i in range(n):
    t = []
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(len(x)):
        for j in range(i,len(y)):
            if i != j:
                t = abs(x[j]-x[i])**d+abs(y[j]-y[i])**d
                h.append(t)
print(min(h),max(h))
