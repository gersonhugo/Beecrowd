while True:
    try:
        e = input()
        a1 = int(e[0])
        a2 = int(e[1])
        a3 = int(e[2])
        a4 = int(e[4])
        a5 = int(e[5])
        a6 = int(e[6])
        a7 = int(e[8])
        a8 = int(e[9])
        a9 = int(e[10])
        a10 = int(e[12])
        a11 = int(e[13])

        d1 = (a1 * 1 + a2 * 2 + a3 * 3 + a4 * 4 + a5 * 5 + a6 * 6 + a7 * 7 + a8 * 8 + a9 * 9) % 11
        d2 = (a1 * 9 + a2 * 8 + a3 * 7 + a4 * 6 + a5 * 5 + a6 * 4 + a7 * 3 + a8 * 2 + a9 * 1) % 11
        if d1 == 10:
            d1 = 0
        if d2 == 10:
            d2 = 0

        if d1 == a10 and d2 == a11:
            print("CPF valido")
        else:
            print("CPF invalido")
    except EOFError:
        break
