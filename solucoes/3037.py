n = int(input())
for i in range(n):
    pj = 0
    pm = 0
    for j in range(3):
        e = input().split()
        pj += int(e[0]) * int(e[1])
    for k in range(3):
        e = input().split()
        pm += int(e[0]) * int(e[1])
    if pj >= pm:
        print("JOAO")
    elif pm > pj:
        print("MARIA")
