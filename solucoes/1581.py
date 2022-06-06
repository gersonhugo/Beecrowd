n = int(input())
for i in range(n):
    k = int(input())
    l = []
    for j in range(k):
        l.append(input())

    p = ''
    for c in range(len(l)-1):
        if l[c] == l[c+1]:
            p = l[c]
        else:
            p = "ingles"
            break
    print(p)
