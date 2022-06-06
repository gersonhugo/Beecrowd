e = input()
l = []
for k in e:
    if k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u':
        l.append(k)

nl = []
for i in range(len(l)-1, -1, -1):
    nl.append(l[i])

if l == nl:
    print('S')
else:
    print('N')
