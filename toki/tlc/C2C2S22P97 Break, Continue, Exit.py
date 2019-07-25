n = int(input())
for i in range(1,n+1):
    if i != 93 and i % 10 != 0:
        print(i)
    elif i == 93:
        print('ERROR')
        break
    else:
        continue
