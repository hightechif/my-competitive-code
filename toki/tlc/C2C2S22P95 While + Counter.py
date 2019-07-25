j = 0
while True:
    try:
        a = int(input())
        j += a
    except EOFError:
        break
print(j)
