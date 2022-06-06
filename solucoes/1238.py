n = int(input())
for i in range(n):
    e = input().split()
    p1 = e[0]
    p2 = e[1]
    if len(p1) < len(p2):
        m = p1
        a = p2
    else:
        m = p2
        a = p1
    l = []
    for j in range(len(m)):
        l.append(p1[j]+p2[j])
    for k in range(len(m), len(a)):
        l.append(a[k])
    print(''.join(l))