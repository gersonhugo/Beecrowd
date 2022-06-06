while True:
    try:
        v = float(input())
        d = float(input())
        r = d/2
        p = 3.14
        a = p*r**2
        h = v/(p*r**2)

        print("ALTURA = {:.2f}".format(h))
        print("AREA = {:.2f}".format(a))
    except EOFError:
        break