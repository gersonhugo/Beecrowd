e = input().split()
x = int(e[0])
y = int(e[1])
j = 1
f = x+1
while True:
    l = []
    for i in range(j,f):
        l.append(i)
    print(*l)

    if l[-1] >= y:
        break
    j+=x
    f+=x

    if f > y:
        f = y+1