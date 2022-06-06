c = 1
while c == 1:

    while True:
        n = float(input())
        if  0 <= n <=10:
            x = n
            break
        else:
            print('nota invalida')

    while True:
        n = float(input())
        if 0 <= n <= 10:
            y = n
            break
        else:
            print('nota invalida')

    m = (x+y)/2
    print('media = {:.2f}'.format(m))

    while True:
        print('novo calculo (1-sim 2-nao)')
        c = int(input())
        if c == 1 or c ==2:
            break