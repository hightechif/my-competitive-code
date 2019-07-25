while True:
    try:
        line = str(input())
    except EOFError:
        break
    print(line)
