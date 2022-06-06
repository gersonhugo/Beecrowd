while True:
    try:
        e = input()
        if e[:1] == "e":
            print("ingles")
        elif e[:1] == "d":
            print("frances")
        elif e[:1] == "n":
            print("portugues")
        elif e[:1] == "a":
            print("caiu")
    except EOFError:
        break
