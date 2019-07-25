def e(n=100):
    sum=0.0
    fac=1.0
    for i in range(1, n+1):
        sum+=(1/fac)
        fac*=i
    return sum

