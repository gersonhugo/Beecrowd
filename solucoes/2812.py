n = int(input())
for i in range(n):
    m = int(input())
    e = input().split()

    l = []
    for k in e:
        if int(k) % 2 != 0:
            l.append(int(k))

    nl = []
    if len(l) > 0:
        l.sort()

        if len(l) % 2 != 0:
            r = int(len(l) / 2) + 1
        else:
            r = int(len(l) / 2)

        for j in range(r):
            nl.append(l[-1 - j])
            if len(nl) == len(l):
                break
            nl.append(l[j])

    if len(nl) > 0:
        print(*nl)
    else:
        print()
