# P27ROtasiMatriks.py : program utk merotasi suatu matriks.
# Ridhan Fadhilah, 07-04-2016

x,y = map(int, input().split())
k = [list(map(int, input().split())) for i in range(x)]
for i in range(y):
    for j in range(1,x+1):
        if j != x:
            print(k[-j][i], end=' ')
        else:
            print(k[-j][i], end='\n')
