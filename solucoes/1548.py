n = int(input())
for i in range(n):
    m = int(input())
    e = input().split()
    l = []
    for k in e:
        l.append(int(k))
    l.sort(reverse=True)

    s = 0
    for j in range(m):
        if int(e[j]) == l[j]:
            s += 1
    print(s)
