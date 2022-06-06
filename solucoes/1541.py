while True:
    e = input()
    if e == '0': break
    else: e = e.split()

    a, b, c = int(e[0]), int(e[1]), int(e[2])
    x = int((100*a*b/c)**(1/2))
    print(x)