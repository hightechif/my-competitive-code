b = input().split()
s = 0
for i in range(1,int(b[0])+1):
    b[i] = int(b[i])
    s = s + b[i]
print(s)
