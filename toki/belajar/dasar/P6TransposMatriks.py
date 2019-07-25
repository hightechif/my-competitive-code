# P6TransposMatriks.py : program utk menghitung transpos matriks.
# Ridhan Fadhilah, 10-12-2015

##list1 = []
##list2 = []
##for i in range(3):
##    c,d = map(str, input().split())
##    list1.append(c)
##    list2.append(d)
##x = list(list1+list2)

# kode diatas dapat disingkat menjadi
x = list(zip(*[list(map(str, input().split())) for i in range(3)]))
b = 1
for i in x:
    for j in i:
        if b % 3 == 0:
            print(int(j), end='\n')
            b+=1
        else:
            print(int(j), end=' ')
            b+=1
