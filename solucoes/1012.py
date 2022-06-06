v = input()
l = v.split()
a = float(l[0])
b = float(l[1])
c = float(l[2])
tri = a * c / 2
cir = 3.14159 * c ** 2
tra = (a + b) * c / 2
qua = b ** 2
ret = a * b
print('TRIANGULO: {:.3f}'.format(tri))
print('CIRCULO: {:.3f}'.format(cir))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(ret))
