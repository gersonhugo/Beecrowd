while True:
    t = int(input())
    if t == 0:
        break

    s = 0
    for i in range(t):
        e = input().split()

        if e[1] == "mamao":
            s+= int(e[0]) * 85
        elif e[1] == "manga":
            s += int(e[0]) * 56
        elif e[1] == "laranja":
            s += int(e[0]) * 50
        elif e[1] == "brocolis":
            s += int(e[0]) * 34
        elif e[1] == "goiaba":
            s += int(e[0]) * 70
        elif e[1] == "morango":
            s += int(e[0]) *85
        elif e[1] == "suco":
            s += int(e[0]) *120

    if s > 130:
        s-= 130
        print("Menos {} mg".format(s))
    elif s < 110:
        s = 110 - s
        print("Mais {} mg".format(s))
    else:
        print("{} mg".format(s))
