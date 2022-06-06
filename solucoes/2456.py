n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
e = int(n[4])

if a < b < c < d < e:
    print('C')
elif a > b > c > d > e:
    print('D')
else:
    print('N')
