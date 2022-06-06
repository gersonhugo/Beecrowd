c = 0
while True:
    n = int(input())

    if n == 0:
        break

    c += 1
    e = input()
    l = []
    o = []

    for k in e:
        if k == '+':
            o.append('+')
            l.append(' ')
        elif k == '-':
            o.append('-')
            l.append(' ')
        else:
            l.append(k)

    d = ''.join(l).split()

    s = int(d[0])
    for i in range(n-1):
        if o[i] == '+':
            s += int(d[i + 1])
        else:
            s -= int(d[i + 1])

    print("Teste", c)
    print(s)
    print()
