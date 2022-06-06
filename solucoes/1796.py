q = int(input())
e = input().split()
s = 0
for k in e:
    if k == '0':
        s += 1

if q % 2 != 0:
    m = (q-1) / 2
else:
    m = q / 2

if s > m:
    print('Y')
else:
    print('N')
