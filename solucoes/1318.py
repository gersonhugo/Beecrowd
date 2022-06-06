while True:
    e = input().split()
    if int(e[0]) == 0 and int(e[1]) == 0:
        break

    l = input().split()
    m = int(e[1])

    for i in range(m):
        l[i] = int(l[i])

    l.sort()

    c = 0
    s = 0

    while c < m:
        a = False
        for j in range(c+1, m):
            if l[j] == l[c]:
                a = True
                c+= 1
            else:
                break
        if a:
            s += 1
        else:
            c += 1

    print(s)
