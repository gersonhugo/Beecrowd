while True:
    try:
        e = input().split()
        h = int(e[0])
        o = int(e[1])
        print(abs(o-h))
    except EOFError:
        break
