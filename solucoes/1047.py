e = input().split()
hi = int(e[0])
mi = int(e[1])
hf = int(e[2])
mf = int(e[3])

dh = hf - hi
dm = mf - mi

if dh == 0 and dm == 0:
    dh = 24
    dm = 0

elif dh == 0 and dm < 0:
    dm += 60
    dh += 23

elif dh < 0 and dm < 0:
    dh += 23
    dm += 60

elif dh > 0 and dm < 0:
    dh -= 1
    dm += 60

elif dh < 0 and dm >= 0:
    dh += 24

print('O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)'.format(dh, dm))