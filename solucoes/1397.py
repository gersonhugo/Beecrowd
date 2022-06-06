while True:
    n = int(input())
    if n == 0:
        break

    x = 0
    y = 0
    for i in range(n):
        e = input().split()
        a = int(e[0])
        b = int(e[1])

        if a > b:
            x += 1
        elif a < b:
            y += 1

    print(x, y)
