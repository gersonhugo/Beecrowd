while True:
    k = int(input())
    if k == 0:
        break
    c = input().split()
    x = int(c[0])
    y = int(c[1])
    for i in range(k):
        e = input().split()
        n = int(e[0])
        m = int(e[1])

        if n == x or m == y:
            print("divisa")
        elif n < x and m > y:
            print("NO")
        elif n > x and m > y:
            print("NE")
        elif n > x and m < y:
            print("SE")
        else:
            print("SO")
