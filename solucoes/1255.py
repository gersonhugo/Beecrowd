a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
     "x", "y", "z", ]
n = int(input())
for i in range(n):
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    e = input()

    for k in e:
        if k == "a" or k == "A":
            l[0] += 1

        elif k == "e" or k == "E":
            l[4] += 1

        elif k == "o" or k == "O":
            l[14] += 1

        elif k == "b" or k == "B":
            l[1] += 1

        elif k == "c" or k == "C":
            l[2] += 1

        elif k == "d" or k == "D":
            l[3] += 1

        elif k == "f" or k == "F":
            l[5] += 1

        elif k == "g" or k == "G":
            l[6] += 1

        elif k == "h" or k == "H":
            l[7] += 1

        elif k == "i" or k == "I":
            l[8] += 1

        elif k == "j" or k == "J":
            l[9] += 1

        elif k == "k" or k == "K":
            l[10] += 1

        elif k == "l" or k == "L":
            l[11] += 1

        elif k == "m" or k == "M":
            l[12] += 1

        elif k == "n" or k == "N":
            l[13] += 1

        elif k == "p" or k == "P":
            l[15] += 1

        elif k == "q" or k == "Q":
            l[16] += 1

        elif k == "r" or k == "R":
            l[17] += 1

        elif k == "s" or k == "S":
            l[18] += 1

        elif k == "t" or k == "T":
            l[19] += 1

        elif k == "u" or k == "U":
            l[20] += 1

        elif k == "v" or k == "V":
            l[21] += 1

        elif k == "w" or k == "W":
            l[22] += 1

        elif k == "x" or k == "X":
            l[23] += 1

        elif k == "y" or k == "Y":
            l[24] += 1

        elif k == "z" or k == "Z":
            l[25] += 1

    m = max(l)
    le = []

    for j in range(26):
        if l[j] == m:
            le.append(a[j])

    print(''.join(le))
