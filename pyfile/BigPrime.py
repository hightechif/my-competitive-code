def sieve(n):
    n += 1
    x = [1]*(n)
    x[0] = 0
    x[1] = 0
    for i in range(2,int(n**0.5+1)):
        j = 2*i
        while j<n:
            x[j] = 0
            j += i
    return x

while True:
    try:
        N = int(input())
        prime = sieve(N)
        while prime[N] != 1:
            N -= 1
        big = N
        print(big)
    except EOFError:
        break
