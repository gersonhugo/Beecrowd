t = 1
while True:
    n = int(input())
    if n == 0:
        break

    l = []
    for i in range(n):
        e = input().split()
        c = int(e[0])
        m = int(e[1])
        l.append((c, m))

    maior = l[0]
    for i in range(1, len(l)):
        if l[i][1] > maior[1]:
            maior = l[i]

    nl = []
    for k in l:
        if k[1] == maior[1]:
            pass
        nl.append(k[0])
    print("Turma {}".format(t))
    print(*nl, '')
    print()

    t += 1
