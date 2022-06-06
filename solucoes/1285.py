while True:
    try:
        e = input().split()
        a = int(e[0])
        b = int(e[1])
        s = b - a + 1

        for i in range(a, b + 1):
            a = False
            si = str(i)
            lsi = len(si)

            for j in range(lsi - 1):
                for k in range(j + 1, lsi):
                    if si[j] == si[k]:
                        a = True
                        break
                if a:
                    s -= 1
                    break

        print(s)
    except EOFError:
        break
