b = int(input())
g = int(input())
if g % 2 != 0:
    g -= 1
f = g / 2 - b
if f <= 0:
    print('Amelia tem todas bolinhas!')
else: print('Faltam {:.0f} bolinha(s)'.format(f))
