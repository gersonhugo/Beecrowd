while True:
    try:
        n = int(input())
        l = []
        for i in range(n):
            l.append(int(input()))
        l.sort()
        for k in l:
            print("{:0>4}".format(k))
    except EOFError:
        break
