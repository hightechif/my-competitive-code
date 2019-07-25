n = int(input())
for i in range(n):
    R,H = map(float, input().split())
    h = ((3.124001*(H**2)*((R**2+H**2)**0.5))/R)**(1/3.0)
    if h>H:
        h=H
    print("%.6f" % h)
