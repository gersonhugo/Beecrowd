while True:
    try:
        n = int(input())
        e = input().split()
        l = []
        for i in range(n):
            l.append(int(e[i]))
        if max(l) < 10:
            print(1)
        elif 10 <= max(l) < 20:
            print(2)
        else:
            print(3)
    except EOFError: break