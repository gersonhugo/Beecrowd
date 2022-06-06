v = input().split()
#o = sort()
v[0] = float(v[0])
v[1] = float(v[1])
v[2] = float(v[2])
v.sort(reverse=True)
a = v[0]
b = v[1]
c = v[2]
if a >= (b+c):
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > (b**2 +c**2):
        print('TRIANGULO OBTUSANGULO')
    if a**2 < (b**2 +c**2):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if a == b != c or b == c != a or a == c != b:
        print('TRIANGULO ISOSCELES')