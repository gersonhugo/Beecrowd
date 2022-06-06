while True:
    try:
        n = int(input())
        r = 0
        for i in range(1, n+1):
            e = input().split()
            t = int(e[0])
            d = int(e[1])
            v = d/t
            if v > r:
                print(i)
                r = v
    except EOFError:
        break
