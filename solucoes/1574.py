r = "RIGHT"
l = "LEFT"
t = int(input())
for i in range(t):
    o = ['']
    p = 0
    n = int(input())
    for j in range(n):
        c = input()
        if c == l:
            o.append(l)
            p -= 1
        elif c == r:
            o.append(r)
            p += 1
        else:
            c = c.split()
            if o[int(c[2])] == l:
                o.append(l)
                p -= 1
            else:
                o.append(r)
                p += 1
    print(p)
