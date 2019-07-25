a = input().split()
k = ''
for i in range(1,int(a[0])+1):
    if i % int(a[1]) == 0:
        k += '*'
    else:
        k += str(i)
    if i < int(a[0]):
        k += ' '
print(k)
