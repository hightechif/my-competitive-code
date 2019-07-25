n = int(input())
if n > 1 and n <= 2**16:
    while n > 2:
        n = n/2
    if n % 2 == 0:
        print('ya')
    else:
        print('bukan')
elif n == 1:
    print('ya')
