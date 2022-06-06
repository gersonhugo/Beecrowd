h = input().split()
i = int(h[0])
f = int(h[1])
if i < f:
    d = f - i
    print('O JOGO DUROU {:.0f} HORA(S)'.format(d))
elif i == f:
    print('O JOGO DUROU 24 HORA(S)')
else:
    d = (f+24) - i
    print('O JOGO DUROU {:.0f} HORA(S)'.format(d))