while True:
    n = int(input())
    if n == 0:
        break

    e = input().split()

    if int(e[0]) >= int(e[1]):
        p = 0
        s = 1
    else:
        p = 1
        s = 0

    if n > 2:
        for i in range(n):
            if int(e[i]) > int(e[p]):
                p = i

        for j in range(n):
            if int(e[j]) > int(e[s]) and int(e[j]) < int(e[p]):
                s = j

    print(s+1)
