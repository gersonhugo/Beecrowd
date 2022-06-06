n = int(input())
for i in range(n):
    a = float(input())
    r =  (a / (4 * 3.14)) ** (1/2)
    if r < 12:
        c = a * 0.09
        print('vermelho = R$ {:.2f}'.format(c))
    elif 12 <= r <= 15:
        c = a * 0.07
        print('azul = R$ {:.2f}'.format(c))
    elif r > 15:
        c = a * 0.05
        print('amarelo = R$ {:.2f}'.format(c))