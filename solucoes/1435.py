while True:
    n = int(input())
    if n == 0: break
    m = []
    for i in range(n * n):
        m.append(i)

    a = 0
    b = n * n
    c = n
    d = 1

    while True:
        for i in range(a, b, n):
            for j in range(c):
                m[i + j] = '{:>3}'.format(d)
        if d > n - 1: break
        a += n + 1
        b -= n
        c -= 2
        d += 1

    for i in range(0, n * n, n):
        print(*m[i:i + n])
    print()