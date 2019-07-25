selisihMin = 400001
n,x = map(int, input().split())
listn = list(map(int, input().split()))
listn.sort()
if len(listn) == 1:
    print(listn[0])
else:
    for i in listn:
        if abs(x-i) < selisihMin:
            selisihMin = abs(x-i)
            hasil = i
    print(hasil)
