n = int(input())
for i in range(n):
    e = input()
    l = []
    c = 0
    for j in range(len(e)):
        if e[j] != '.':
            l.append(e[j])
    j= 0
    if len(l) == 0 or 1 == len(l):
        print(0)
    else:
        while True:
            if l[j] == '<' and l[j+1] == '>':
                l.pop(j)
                l.pop(j)
                c += 1
                if j > 0:
                    j = 0
            else:
                j += 1
            if not l or j == len(l)-1:
                break
        print(c)
