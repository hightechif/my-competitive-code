def nilai(x):
    i = 1
    while x != 1:
        i += 1
        if x % 2 != 0:
            x = 3*x+1
        else:
            x = x/2
    return i
while True:
    try:
        n = list(map(int, input().split()))
        a,b,k = (n[0],n[1],1)
        for i in range(a,b+1):
            l = nilai(i)
            if k > l:
                continue
            else:
                k = l
        print(a,b,k)
    except EOFError:
        break
