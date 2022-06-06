n = int(input())
c = 0
e = 0
tc = 0
te = 0

for i in range(n):
    x = input().split()

    if x[0] == 'chuva' and tc == 0:
        c += 1
        te += 1
    elif x[0] == 'chuva' and tc != 0:
        tc -= 1
        te += 1

    if x[1] == 'chuva' and te == 0:
        e += 1
        tc += 1
    elif x[1] == 'chuva' and te != 0:
        te -= 1
        tc += 1

print(c, e)
