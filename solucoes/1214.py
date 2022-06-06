c = int(input())
for i in range(c):
    e = input().split()

    s = 0
    t = int(e[0])
    for j in range(1, t+1):
        e[j] = int(e[j])
        s += e[j]

    m = s / t
    a = 0
    for k in range(1, t+1):
        if e[k] > m:
            a += 1
    p = a * 100 / t

    print("{:.3f}%".format(p))
