s1="............"
s2=".####..#...."
s3=".#...#.#...."
s4=".#...#.#...."
s5=".####..#...."
s6=".#...#.#...."
s7=".#...#.#...."
s8=".####..#####"
s9="............"
daftar = [s1,s2,s3,s4,s5,s6,s7,s8]
R,C = map(int, input().split())
for i in range(len(daftar)):
    daftar[i] *= (C)
    daftar[i] += "."
s9=s9*(C)
s9=s9+"."
for i in range(R):
    for j in daftar:
        print(j)
print(s9)
