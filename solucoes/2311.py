n = int(input())
for i in range(n):
    nm = input()
    g = float(input())
    l = input().split()

    for j in range(len(l)):
        l[j] = float(l[j])
    l.sort()
    l.pop(0)
    l.pop(-1)

    s = 0
    for k in l:
        s += float(k)

    print("{} {:.2f}".format(nm, s * g))
