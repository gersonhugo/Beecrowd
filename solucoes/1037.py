i = float(input())
if i >= 0 and i <= 25:
    if i == 0 or i == 25:
        print('Intervalo [0,25]')
    else:
        print('Intervalo (0,25]')
elif i > 25 and i <= 50:
    print('Intervalo (25,50]')
elif i > 50 and i <= 75:
    print('Intervalo (50,75]')
elif i > 75 and i <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
