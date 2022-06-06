c = 0
while True:
    try:
        e = int(input())
        c += 1

        if e != 0:
            s = 1
            l = [0]
            for i in range(e+1):
                for j in range(i):
                    s += 1
                    l.append(i)
            print("Caso {}: {} numeros".format(c, s))
            print(*l)
        else:
            print("Caso {}: 1 numero".format(c, s))
            print(0)

        print()
    except EOFError:
        break
