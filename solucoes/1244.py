n = int(input())
for j in range(n):
    e = input()
    l = []
    p = 0
    for i in range(len(e)):
        if e[i] == ' ':
            l.append(e[p:i])
            p = i + 1
    l.append(e[p:len(e)])

    t = len(l)
    c = 0

    while c < t-1:
        for i in range(c, t):
            if len(l[i]) > len(l[c]):
                l.insert(c, l[i])
                l.pop(i+1)
        c += 1
    print(*l)
