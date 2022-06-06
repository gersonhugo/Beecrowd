n = int(input())
l = []

for i in range(n):
    l.append(input())

for i in range(1, n):
    for j in range(1, n):
        if l[j][0] < l[j-1][0]:
            nome = l[j]
            l.pop(j)
            l.insert(j - 1, nome)

for s in l:
    print(s)
