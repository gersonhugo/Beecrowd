i = input()
l = i.split()
a = int(l[0])
b = int(l[1])
c = int(l[2])
d = int(l[3])
if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
