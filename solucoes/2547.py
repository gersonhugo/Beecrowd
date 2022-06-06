while True:
    try:
        e = input().split()
        n = int(e[0])
        mi = int(e[1])
        ma = int(e[2])

        s = 0
        for i in range(n):
            e = int(input())
            if e >= mi and e <= ma:
                s += 1
        print(s)
    except EOFError:
        break
