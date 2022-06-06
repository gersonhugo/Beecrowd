c = 0
while True:
    n = int(input())
    if n == 0:
        break

    c += 1
    l = []
    for i in range(n):
        l.append(input())

    t = 0

    for k in l:
        if len(k) > t:
            t = len(k)

    if c > 1:
        print()

    for j in l:
        print(' ' * (t - len(j)) + j)
