while True:
    try:
        e = input()
        a1 = int(e[0])
        a2 = int(e[1])
        a3 = int(e[2])
        a4 = int(e[3])
        a5 = int(e[4])
        a6 = int(e[5])
        a7 = int(e[6])
        a8 = int(e[7])
        a9 = int(e[8])

        d1 = (a1 * 1 + a2 * 2 + a3 * 3 + a4 * 4 + a5 * 5 + a6 * 6 + a7 * 7 + a8 * 8 + a9 * 9) % 11
        d2 = (a1 * 9 + a2 * 8 + a3 * 7 + a4 * 6 + a5 * 5 + a6 * 4 + a7 * 3 + a8 * 2 + a9 * 1) % 11
        if d1 == 10:
            d1 = 0
        if d2 == 10:
            d2 = 0

        print(str(a1)+str(a2)+str(a3)+'.'+str(a4)+str(a5)+str(a6)+'.'+str(a7)+str(a8)+str(a9)+'-'+str(d1)+str(d2))
    except EOFError:
        break
