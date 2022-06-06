while True:
    n = int(input())
    if n == 0: break
    m = []
    d = 1
    e = 2
    t = len(str(4**(n-1)))
    for l in range(0, n*n, n):
        for c in range(n):
            m.append(str(d).rjust(t))
            if c == n-1:
                d = e
                e *= 2
            else:
                d*=2
    for i in range(0,n*n, n):
        print(*m[i:i + n])
    print()