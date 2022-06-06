o = input()
l = []
s = 0
p = 23
f = 132
for i in range(144):
    e = float(input())
    l.append(e)
for i in range(5):
    for j in range(p, f, 12):
        s+= l[j]
    p+=11
    f-=13

m = s / 30
if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(m))