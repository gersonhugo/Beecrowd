s = float(input())
if s <= 2000:
    print('Isento')
else:
    aplicavel = s-2000
    if s >= 2000.01 and s <= 3000:
        imposto = (s - 2000) * 0.08
    elif s >= 3000.01 and s <= 4500:
        aplicavel -= 1000
        taxa = 1000 * 0.08
        imposto = aplicavel * 0.18 + taxa
    elif s > 4500:
        aplicavel -= 2500
        taxa = 1000 * 0.08 + 1500 * 0.18
        imposto = aplicavel * 0.28 + taxa

    print('R$ {:.2f}'.format(imposto))