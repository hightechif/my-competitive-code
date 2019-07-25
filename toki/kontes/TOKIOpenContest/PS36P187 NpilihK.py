N, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
j = 10**9
for i in range(N-K+1):
    j = min(j,data[i+K-1]-data[i])
print(j)
