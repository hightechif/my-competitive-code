def AP(x):
    bts = int(x**0.5)
    count = 0
    for i in range(2,bts+1):
        if x % i == 0:
            if count > 0:
                return False
            else:
                count += 1
    return True

n = int(input())
for i in range(n):
    if AP(int(input())):
        print('YA')
    else:
        print('BUKAN')
