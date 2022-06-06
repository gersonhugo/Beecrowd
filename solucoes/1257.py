n = int(input())
for i in range(n):
    l = int(input())
    a = []

    for j in range(l):
        e = input()
        for k in range(len(e)):
            a.append(ord(e[k]) - 65 + j + k)
    s = 0
    for k in a:
        s += k
    print(s)
