from math import fabs
v = input()
l = v.split()
a = int(l[0])
b = int(l[1])
c = int(l[2])
m1 = int(((a+b) + fabs(a-b))/2)
m2 = int(((m1+c) + fabs(m1-c))/2)
print(int(m2), 'eh o maior')
