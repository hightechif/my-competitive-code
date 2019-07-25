x = []
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
q = int(input())
for i in range(q):
    x.append(input().split())
for j in x:
    if j[0] == 'A':
        if j[2] == 'A':
            temp = a[int(j[1])-1]
            a[int(j[1])-1] = a[int(j[3])-1]
            a[int(j[3])-1] = temp
        else:
            temp = a[int(j[1])-1]
            a[int(j[1])-1] = b[int(j[3])-1]
            b[int(j[3])-1] = temp
    else:
        if j[2] == 'A':
            temp = b[int(j[1])-1]
            b[int(j[1])-1] = a[int(j[3])-1]
            a[int(j[3])-1] = temp
        else:
            temp = b[int(j[1])-1]
            b[int(j[1])-1] = b[int(j[3])-1]
            b[int(j[3])-1] = temp
for i in range(len(a)-1):
    print(a[i], end=' ')
print(a[-1])
for j in range(len(b)-1):
    print(b[j], end=' ')
print(b[-1])
