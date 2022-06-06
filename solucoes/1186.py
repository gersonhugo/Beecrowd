o = input()
l = []
s = 0
p = 23
f = 24
for i in range(144):
    e = float(input())
    l.append(e)
for i in range(11):
    for j in range(p, f):
        s+= l[j]
    p+=11
    f+=12

m = s / 66
if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(m))