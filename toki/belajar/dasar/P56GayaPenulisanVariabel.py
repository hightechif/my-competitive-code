alfabet = list(map(chr, range(65, 91)))
sinput = input()
s = sinput
while "_" in s:
    if "_" == s[-1]:
        s = s[:len(s)-1]
    else:
        idx = s.index("_")
        s = s[:idx]+s[idx+1].upper()+s[idx+2:]
s1 = s
for i in s:
    if i in alfabet:
        idx = s.index(i)
        s = s[:idx]+"_"+s[idx].lower()+s[idx+1:]
s2 = s
if s2 == sinput:
    print(s1)
elif s1 == sinput:
    print(s2)
else:
    print(sinput)
