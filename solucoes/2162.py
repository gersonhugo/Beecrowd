n = int(input())
e = input().split()

for i in range(n):
    e[i] = int(e[i])

s = ''

if e[0] < e[1]:
    s = 'p'
elif e[0] > e[1]:
    s = 'v'

if s == '':
    print(0)
else:
    r = True
    for i in range(1, n-1):
        if s == 'p':
            if e[i] > e[i + 1]:
                s = 'v'
            else:
                r = False
                break
        elif s == 'v':
            if e[i] < e[i + 1]:
                s = 'p'
            else:
                r = False
                break
        if e[i] == e[i + 1]:
            r = False
            break
    if r:
        print(1)
    else:
        print(0)
