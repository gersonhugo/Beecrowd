abc = input().split()
a = float(abc[0])
b = float(abc[1])
c = float(abc[2])
d = b**2 -4*a*c

if a == 0 or d < 0:
    print('Impossivel calcular')
else:
    r1 = (-b + d**(1/2))/(2*a)
    r2 = (-b - d**(1/2))/(2*a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
