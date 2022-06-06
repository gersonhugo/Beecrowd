while True:
    e = input().split()
    n = int(e[0])
    m = int(e[1])

    if n == 0 and m == 0:
        break

    t = m - n

    if t < 4 or t > 200:
        print("impossible")

    elif t / 2 == 2 or t / 2 == 5 or t / 2 == 10 or t / 2 == 20 or t / 2 == 50 or t / 2 == 100:
        print("possible")

    else:
        c = 0
        for i in range(1):
            if t > 100:
                t -= 100
                c += 1

            if t >= 50:
                t -= 50
                c += 1

            if c == 2:
                break

            if t >= 20:
                t -= 20
                c += 1

            if c == 2:
                break

            if t >= 10:
                t -= 10
                c += 1

            if c == 2:
                break

            if t >= 5:
                t -= 5
                c += 1

            if c == 2:
                break

            if t >= 2:
                t -= 2
                c += 1

        if c == 2 and t == 0:
            print("possible")
        else:
            print("impossible")
