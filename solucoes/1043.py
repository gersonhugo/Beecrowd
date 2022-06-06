v = input().split()
a = float(v[0])
b = float(v[1])
c = float(v[2])
l = sorted(v)
lmenor1 = float(l[0])
lmenor2 = float(l[1])
lmaior = float(l[2])
if (lmenor1 + lmenor2) > lmaior:
    p = a+b+c
    print('Perimetro = {:.1f}'.format(p))
else:
    t = (a+b)*c/2
    print('Area = {:.1f}'.format(t))