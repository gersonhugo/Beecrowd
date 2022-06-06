n = 1
while True:
    n = int(input())

    if n == 0: break

    m = []
    for l in range(n*n):
        m.append('')

    p = 0
    a = n
    for t in range(n):
        v = 1
        for l in range(p, a+p):
            m[l] = '{:>3}'.format(v)
            v+=1
        v-=a
        for c in range(n+p,(n*n),n):
            m[c] = '{:>3}'.format(v+1)
            v += 1

        p+=n+1
        a-=1
    for i in range(0, n*n, n):
        print(*m[i:i+n])
    print()