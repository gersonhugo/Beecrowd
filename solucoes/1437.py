while True:
    n = int(input())
    if n == 0:
        break

    e = input()
    s = 0
    for k in e:
        if k == "D":
            s += 90
        else:
            s -= 90

    if s >= 360 or s <= -360:
        s = s % 360

    if s == 0:
        print("N")
    elif s == 90 or s == -270:
        print("L")
    elif s == 180 or s == -180:
        print("S")
    elif s == 270 or s == -90:
        print("O")
