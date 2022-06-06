while True:
    try:
        t = int(input())
        m = float(input())
        for i in range(t-1):
            e = float(input())
            if e < m:
                m = e
        print("{:.2f}".format(m))

    except EOFError:
        break
