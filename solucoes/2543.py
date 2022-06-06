while True:
    try:
        e = input().split()
        n = int(e[0])
        l = e[1]

        s = 0
        for i in range(n):
            e = input().split()
            if e[0] == l:
                if e[1] == '0':
                    s += 1
        print(s)

    except EOFError:
        break
