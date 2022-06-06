while True:
    try:
        e = input().split(":")
        h = int(e[0])
        m = int(e[1])

        ah = (h - 7) * 60
        am = m

        if ah < 0:
            ah = 0
            am = 0

        print("Atraso maximo: {}".format(ah + am))

    except EOFError:
        break