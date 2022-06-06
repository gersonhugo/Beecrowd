c = 0
nc = int(input())
for i in range(nc):
    c += 1
    e = input().split()
    n = int(e[0])
    s = int(e[1])
    l = []
    for j in range(1, n + 1):
        l.append(j)

    ini = -1
    while len(l) > 1:
        print(l)
        for k in range(ini, len(l)+1, s):
            print('k', k+s)
            if k+s >= len(l):
                break
            l.pop(k+s)

            break
            #     l.insert(0, l[k-1])
            #     print("insert", l)
            #     l.pop(k)
            #     ini = s
            #     break
            # else:
            #     l.pop(k)
            #     ini = k+1
            #     break

            print(l)

    print("Case {}: {}".format(c, l))
