count = 1
while True:
    try:
        kalimat = input()
        for i in kalimat:
            if i == "\"" and count % 2 != 0:
                idx = kalimat.index(i)
                kalimat = kalimat[:idx]+"``"+kalimat[idx+1:]
                count += 1
            elif i =="\"" and count % 2 == 0:
                idx = kalimat.index(i)
                kalimat = kalimat[:idx]+"\'\'"+kalimat[idx+1:]
                count += 1
        print(kalimat)
    except EOFError:
        break
