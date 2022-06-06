while True:
    d = input().split()
    x = int(d[0])
    y = int(d[1])
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
    else: break