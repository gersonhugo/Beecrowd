n = int(input())
for i in range(n):
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    e = input()

    for k in e:
        if k == "a":
            l[0] = 1

        elif k == "e":
            l[4] = 1

        elif k == "o":
            l[14] = 1

        elif k == "s":
            l[18] = 1

        elif k == "r":
            l[17] = 1

        elif k == "i":
            l[8] = 1

        elif k == "n":
            l[13] = 1

        elif k == "d":
            l[3] = 1

        elif k == "m":
            l[12] = 1

        elif k == "u":
            l[20] = 1

        elif k == "t":
            l[19] = 1

        elif k == "c":
            l[2] = 1

        elif k == "l":
            l[11] = 1

        elif k == "p":
            l[15] = 1

        elif k == "v":
            l[21] = 1

        elif k == "g":
            l[6] = 1

        elif k == "h":
            l[7] = 1

        elif k == "q":
            l[16] = 1

        elif k == "b":
            l[1] = 1

        elif k == "f":
            l[5] = 1

        elif k == "z":
            l[25] = 1

        elif k == "j":
            l[9] = 1

        elif k == "x":
            l[23] = 1

        elif k == "k":
            l[10] = 1

        elif k == "w":
            l[22] = 1

        elif k == "y":
            l[24] = 1

    s = 0
    for j in range(26):
        s += l[j]

    if s == 26:
        print("frase completa")
    elif s >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
