n = int(input())
for i in range(n):
    l = []
    x = int(input())
    for j in range(1, x):
        if x % j == 0:
            l.append(j)
    s = 0
    for k in range(len(l)):
        s+= l[k]
    if x == s: print('{} eh perfeito'.format(x))
    else: print('{} nao eh perfeito'.format(x))