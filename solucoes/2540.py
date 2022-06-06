while True:
    try:
        n = int(input())
        v = input().split()
        cont = 0
        for i in range(len(v)):
            if v[i] == '1':
                cont += 1
        if cont >= n*2/3:
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break