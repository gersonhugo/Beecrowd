n = int(input())
g = 0
v = 0
for i in range(n):
    e = input().split()
    t = e[0]
    c = int(e[1])

    if t == 'G':
        g += c
    else:
        v += c

if g > v:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")