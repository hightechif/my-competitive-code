n,m = map(int, input().split())
uji = [i for i in range(1,n+1)]
L = 0
R = n
for i in range(m):
    s = input()
    if s[7:11] == "left":
        x = int(s[15:])
        if x <= R:
            R = x - 1
    elif s[7:12] == "right":
        y = int(s[16:])
        if y >= L:
            L = y

tampil = R - L
if tampil < 1:
    print(-1)
else:
    print(tampil)
