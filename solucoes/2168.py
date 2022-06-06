n = int(input())
l = []
for i in range(n+1):
    e = input().split()
    l.append(e)

nl = []
for i in range(n):
    nl.append([])
    for j in range(n):
        s = 0

        if l[i][j] == '1':
            s+= 1

        if l[i][j+1] == '1':
            s+= 1

        if l[i+1][j] == '1':
            s+= 1

        if l[i+1][j+1] == '1':
            s+= 1

        if s < 2:
            nl[i].append('U')
        else:
            nl[i].append('S')

for i in range(0,len(nl),1):
    print(''.join(nl[i]))
