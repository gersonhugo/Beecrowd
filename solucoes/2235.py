e = input().split()
l = []
for i in range(3):
    l.append(int(e[i]))
l.sort()
if l[0] == l[1] or l[1] == l[2]:
    print('S')
elif l[0] + l[1] == l[2]:
    print('S')
else:
    print('N')