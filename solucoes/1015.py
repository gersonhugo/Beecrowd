from math import sqrt
p1 = input()
p2 = input()
l1 = p1.split()
l2 = p2.split()

x1 = float(l1[0])
y1 = float(l1[1])

x2 = float(l2[0])
y2 = float(l2[1])

d = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('{:.4f}'.format(d))
