while True:
    try:
        e = input().split()
        n = int(e[0])
        m = int(e[1])

        f = input().split()

        s = 0

        for i in range(n-1, n-m-1,-1):
            s+= int(f[i])

        print(s)

    except EOFError:
        break
