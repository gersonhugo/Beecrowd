while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        x = input().split()
        a = int(x[0])
        b = int(x[1])
        c = int(x[2])
        d = int(x[3])
        e = int(x[4])
        if a <= 127 and b > 127 and c > 127 and d > 127 and e > 127:
            print("A")
        elif b <= 127 and a > 127 and c > 127 and d > 127 and e > 127:
            print("B")
        elif c <= 127 and a > 127 and b > 127 and d > 127 and e > 127:
            print("C")
        elif d <= 127 and a > 127 and b > 127 and c > 127 and e > 127:
            print("D")
        elif e <= 127 and a > 127 and b > 127 and c > 127 and d > 127:
            print("E")
        else:
            print("*")
