while True:
    try:
        m = int(input())
        a = 0
        b = 0
        for i in range(m):
            e = input().split()
            n = int(e[0])
            c = int(e[1])
            a += n * c
            b += c * 100
        print("{:.4f}".format((a / m) / (b / m)))
    except EOFError:
        break
