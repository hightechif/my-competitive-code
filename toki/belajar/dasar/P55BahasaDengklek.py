alfabet = list(map(chr, range(97, 123)))
news = ""
s = input()
for i in s:
    if i in alfabet:
        news += i.upper()
    else:
        news += i.lower()
print(news)
