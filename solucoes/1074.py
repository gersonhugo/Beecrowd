n = int(input())
p = []
for i in range(n):
    v = int(input())
    p.clear()
    if v == 0:
        p.append('NULL')
    else:
        if v % 2 == 0:
            p.append('EVEN')
        else:
            p.append('ODD')
        if v > 0:
            p.append('POSITIVE')
        elif v < 0:
            p.append('NEGATIVE')
    print(*p)