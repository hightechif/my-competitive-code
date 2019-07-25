s,t = input().split()
while t in s:
    i = s.index(t)
    s = s[:i]+s[i+len(t):]
print(s)
