p1 = input()
p2 = input()
l1 = p1.split()
l2 = p2.split()

c1 = int(l1[0])
n1 = int(l1[1])
v1 = float(l1[2])

c2 = int(l2[0])
n2 = int(l2[1])
v2 = float(l2[2])

valor = (n1*v1) + (n2*v2)

print('VALOR A PAGAR: R$ {:.2f}'.format(valor))
