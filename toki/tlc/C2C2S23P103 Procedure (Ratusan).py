while True:
    try:
        n = len(str(int(input())))
        if n == 1:
            print('satuan')
        elif n == 2:
            print('puluhan')
        elif n == 3:
            print('ratusan')
        elif n == 4:
            print('ribuan')
        elif n == 5:
            print('puluhribuan')
        else:
            break
    except EOFError:
        break
