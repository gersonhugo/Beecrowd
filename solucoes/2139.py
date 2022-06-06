import datetime
while True:
    try:
        e = input().split()
        m = int(e[0])
        d = int(e[1])

        if m == 12 and d == 25:
            print("E natal!")
        elif m == 12 and d == 24:
            print("E vespera de natal!")
        elif m == 12 and d > 25:
            print("Ja passou!")
        else:
            n = datetime.date(2016, 12, 25) - datetime.date(2016,m,d)
            print("Faltam {} dias para o natal!".format(n.days))
    except EOFError:
        break
