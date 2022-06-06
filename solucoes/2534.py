while True:
    try:
        e = input().split()
        n = int(e[0])
        q = int(e[1])

        l = []

        for i in range(n):
            e = int(input())
            l.append(e)

        l.sort(reverse=True)

        for i in range(q):
            e = int(input())
            print(l[e-1])

    except EOFError:
        break
