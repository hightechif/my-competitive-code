def lacakBalik(h,kata):
    idx = 0
    for i in kata:
        if i == h:
            break
        idx += 1
    return idx

operasi = ['+','*','/','-']
x = input()
for i in range(len(operasi)):
    if operasi[i] in x:
        analisis = i
        idxstr = lacakBalik(operasi[i],x)
        break

if analisis == 0:
    print(int(x[:idxstr])+int(x[idxstr+1:]))
elif analisis == 1:
    print(int(x[:idxstr])*int(x[idxstr+1:]))
elif analisis == 2:
    print(int(x[:idxstr])/float(x[idxstr+1:]))
elif analisis == 3:
    print(int(x[:idxstr])-int(x[idxstr+1:]))
