while True:
    try:
        nd = input().split()
        n = int(nd[0])
        d = int(nd[1])
        l = []

        for i in range(d):
            e = input().split()
            l.append(e)

        for c in l:
            r = False
            for i in range(1, n+1):
                if c[i] == "1":
                    r = True
                else:
                    r = False
                    break
            if r:
                print(c[0])
                break

        if not r:
            print("Pizza antes de FdI")

    except EOFError:
        break