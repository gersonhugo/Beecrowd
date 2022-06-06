n = int(input())
for i in range(n):
    e = float(input())
    d = 0
    while e > 1:
        e /= 2
        d += 1
    print(d, "dias")
