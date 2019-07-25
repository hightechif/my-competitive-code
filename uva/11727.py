for i in range(int(input())):
    employ = list(map(int, input().split()))
    employ.sort()
    print("Case %d:" % (i+1),employ[1])
