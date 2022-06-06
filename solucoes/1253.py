a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
for i in range(n):
    e = input()
    p = int(input())
    l = []
    for s in e:
        l.append(a[a.find(s)-p])
    print(''.join(l))