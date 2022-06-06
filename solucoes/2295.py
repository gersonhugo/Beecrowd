e = input().split()
pa = float(e[0])
pg = float(e[1])
ra = float(e[2])
rg = float(e[3])

la = pa / ra
lg = pg / rg

if la < lg:
    print('A')
else:
    print('G')
