m = 'Essa coluna nao existe Tobias!'
while True:
    try:
        e = input()
        if len(e) > 3:
            print(m)
        elif len(e) == 1:
            s = ord(e[0]) - 64
            print(s)
        elif len(e) == 2:
            s = (ord(e[0]) - 64) * 26
            s += ord(e[1]) - 64
            print(s)
        elif len(e) == 3:
            s = (ord(e[0]) - 64) * 676
            s += (ord(e[1]) - 64) * 26
            if s > 16384:
                print(m)
            else:
                s += ord(e[2]) - 64
                if s > 16384:
                    print(m)
                else:
                    print(s)
    except EOFError:
        break
