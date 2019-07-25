def p(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(int(input())):
    q = p(int(input()))
    if q == True:
        print('YA')
    else:
        print('BUKAN')
