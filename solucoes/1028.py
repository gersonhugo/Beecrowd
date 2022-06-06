n = int(input())
for i in range(n):
    e = input().split()
    f1, f2 = int(e[0]), int(e[1])
    a, t = f1, f2
    r = a % t
    while r != 0:
        a = t
        t = r
        r = a % t
    print(t)