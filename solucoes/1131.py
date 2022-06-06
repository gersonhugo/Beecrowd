q = 0
i = 0
g = 0
e = 0
while True:
    n = (input()).split()
    x, y = int(n[0]), int(n[1])
    if x > y:
        i+=1
    elif y > x:
        g+=1
    else:
        e+=1
    print('Novo grenal (1-sim 2-nao)')
    q+=1
    c = int(input())
    if c == 1:
        pass
    elif c == 2:
        print('{} grenais'.format(q))
        print('Inter:{}'.format(i))
        print('Gremio:{}'.format(g))
        print('Empates:{}'.format(e))
        if i == g:
            print('Nao houve vencedor')
        elif i > g:
            v = 'Inter'
            print('{} venceu mais'.format(v))
        elif g > i:
            v = 'Gremio'
            print('{} venceu mais'.format(v))
        break