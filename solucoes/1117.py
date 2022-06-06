notas = []
while True:
    v = float(input())
    if v < 0 or v > 10:
        print('nota invalida')
    else:
        notas.append(v)
        if len(notas) == 2:
            media = (notas[0] + notas[1]) / 2
            print('media = {:.2f}'.format(media))
            break