alfabet = list(map(chr, range(97, 123)))*2
news = ""
s = input()
k = int(input())
for i in s:
    idx = alfabet.index(i)
    news += alfabet[idx+k]
print(news)
