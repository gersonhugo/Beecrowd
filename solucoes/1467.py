while True:
    try:
        e = input().split()
        a = int(e[0])
        b = int(e[1])
        c = int(e[2])

        if a == b and a == c:
            print("*")
        elif a == b and a != c:
            print("C")
        elif a == c and a != b:
            print("B")
        else:
            print("A")
    except EOFError:
        break
