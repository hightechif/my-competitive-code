def konversi(n): # convert a column from number to alphabet
    s = ''
    column = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while n>0:
        if n%26==0:
            n = n//26 -1
            s += 'Z'
        else:
            k = n%26
            n = n//26

            s += column[k-1]

    return s[::-1]

def skonversi(s): # convert a column from alphabet to number
    column = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0

    for l in s:

        k = column.index(l)+1
        i = i*26+k

    return i

for i in range(int(input())):
    s = input()
    n = len(s)
    hasil = ''
    digit = False
    if 'R' in s and 'C' in s: # determine number between R and C
        idxR = s.index('R')
        idxC = s.index('C')
        k = idxR + 1
        while k<idxC:
            if s[k].isdigit():
                digit = True
            else:
                digit = False
            k += 1

    if 'R' in s and 'C' in s and digit: # Find the result
        idxR = s.index('R')
        idxC = s.index('C')
        row = int(s[idxR+1:idxC])
        col = int(s[idxC+1:])
        col = konversi(col)
        hasil = col + str(row)

    else: # Find the result in another form
        col = ''
        j = 0
        while j<n and not s[j].isdigit():
            col += s[j]
            j += 1
        col = skonversi(col)
        row = int(s[j:])
        hasil = 'R'+str(row)+'C'+str(col)

    print(hasil)
