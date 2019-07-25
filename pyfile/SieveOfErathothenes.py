def sieve(n):
    n += 1
    x = [1]*n
    x[0], x[1] = (0,0)
    for i in range(2,int(n**0.5)+1):
        j = 2*i
        while j<n:
            x[j] = 0
            j += i
    return x

N = int(input())
prime = sieve(N)
for j in range(len(prime)): 
    if prime[j] == 1:
        print(j, end=" ")
