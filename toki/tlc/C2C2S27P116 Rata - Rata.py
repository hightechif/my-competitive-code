x = int(input())
A = list(float(input()) for i in range(x))
print('%.2f %.2f %.2f' % (min(A),max(A),(sum(A)/x)))
