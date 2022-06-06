n = int(input())
o = input()
l = []
s = 0
for i in range(144):
    e = float(input())
    l.append(e)
for i in range(n, 144, 12):
    s+= l[i]
m = s / 12
if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(m))