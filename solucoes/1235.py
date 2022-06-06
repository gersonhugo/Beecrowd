n = int(input())
for i in range(n):
    e = input()
    l = []
    if len(e) % 2 == 0:
        r = int((len(e)-1)/2)
    else:
        r = int((len(e)-2)/2)

    for j in range(r, -1, -1):
        l.append(e[j])

    for k in range(len(e)-1, r, -1):
        l.append(e[k])

    print(''.join(l))
