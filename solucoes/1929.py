e = input().split()
l = []

for i in range(4):
    l.append(int(e[i]))

l.sort()

if l[0] + l[1] > l[2]:
    print('S')
elif l[1] + l[2] > l[3]:
    print('S')
else:
    print('N')