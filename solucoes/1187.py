o = input()
l = []
s = 0
p = 1
f = 11
for i in range(144):
    e = float(input())
    l.append(e)
for i in range(5):
    for j in range(p, f):
        s+= l[j]
    p+=13
    f+=11

m = s / 30
if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(m))