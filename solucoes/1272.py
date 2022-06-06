n = int(input())
for i in range(n):
    e = input().split()
    l = []
    for k in e:
        l.append(k[0])
    print(''.join(l))
