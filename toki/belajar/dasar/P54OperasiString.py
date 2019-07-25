s1 = input()
s2 = input()
s3 = input()
s4 = input()
if s2 in s1:
    i = s1.index(s2)
    s1 = s1[:i]+s1[i+len(s2):]
if s3 in s1:
    i = s1.index(s3)
    s1 = s1[:i+len(s3)]+s4+s1[i+len(s3):]
print(s1)
