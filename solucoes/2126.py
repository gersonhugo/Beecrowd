c = 0
while True:
    try:
        n = input()
        e = input()
        c += 1
        s = 0
        p = 0

        for i in range(len(e) - len(n)+1):
            if n == e[i:i + len(n)]:
                s += 1
                p = i+1
        print("Caso #{}:".format(c))
        if s > 0:
            print("Qtd.Subsequencias: {}".format(s))
            print("Pos: {}".format(p))
        else:
            print("Nao existe subsequencia")
        print()

    except EOFError:
        break
