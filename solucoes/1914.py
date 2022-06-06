n = int(input())
for i in range(n):
    j = input().split()
    v = input().split()
    j1, j2 = j[0], j[2]
    s = int(v[0]) + int(v[1])
    if j[1] == 'PAR':
        if s % 2 == 0:
            print(j1)
        else:
            print(j2)
    else:
        if s % 2 == 0:
            print(j2)
        else:
            print(j1)