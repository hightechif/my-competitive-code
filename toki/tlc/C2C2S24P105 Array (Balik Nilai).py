h = []
while True:
    try:
        h.append(int(input()))
    except EOFError:
        break
for i in range(1,len(h)+1):
    print(h[-i])
