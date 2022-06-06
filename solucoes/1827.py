while True:
    try:
        n = int(input())
        if n == 0: break
        m = []
        for i in range(n*n):
            m.append('0')

        # diagonal principal
        for i in range(0, n*n, n+1):
            m[i] = '2'

        # diagonal secundária
        for i in range(n-1, n*n-(n-1), n-1):
            m[i] = '3'

        # parte interna
        p = int(n/3)
        for i in range(0, n-(p*2)):
            for j in range(n*p+p, n*n-(n*p), n):
                m[i+j] = '1'

        # centro
        m[int(((n*n)-1)/2)] = '4'

        for i in range(0, n*n, n):
            print(''.join(m[i:i+n]))
        print()

    except EOFError: break