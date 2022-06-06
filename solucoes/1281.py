n = int(input())
for i in range(n):
    m = int(input())
    l = []
    for j in range(m):
        e = input().split()
        l.append((e[0], float(e[1])))

    p = int(input())
    nl = []
    for k in range(p):
        e = input().split()
        nl.append((e[0], int(e[1])))

    s = 0
    for c in nl:
        for d in l:
            if d[0] == c[0]:
                s += d[1] * c[1]
                break

    print("R$ {:.2f}".format(s))
