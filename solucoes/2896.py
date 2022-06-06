t = int(input())
for i in range(t):
    e = input().split()
    c = int(e[0])
    v = int(e[1])
    if c < v:
        r = c
    else:
        r = c // v + c % v
    print(r)
