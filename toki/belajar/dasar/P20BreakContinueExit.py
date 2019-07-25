# P20BreakContinueExit.py : program pemanfaatan break dan continue.
# Ridhan Fadhilah, 27-12-2015

n = int(input())
for i in range(1,n+1):
    if i == 42:
        print('ERROR')
        break
    elif i % 10 != 0:
        print(i)
    else:
        continue
