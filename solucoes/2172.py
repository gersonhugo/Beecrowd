while True:
    e = input().split()
    x = int(e[0])
    m = int(e[1])
    if x == 0 and m == 0:
        break

    print(x*m)
