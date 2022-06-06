while True:
    p = input().split()
    m, n = int(p[0]), int(p[1])
    if m <= 0 or n <= 0:
        break
    if m < n:
        l = []
        s = 0
        for i in range(m, n+1):
            l.append(i)
            s += i
        print(*l, 'Sum={}'.format(s))
    elif n < m:
        l = []
        s = 0
        for i in range(n, m+1):
            l.append(i)
            s += i
        print(*l, 'Sum={}'.format(s))
    else:
        l = m
        s = m+n
        print(l, 'Sum={}'.format(s))