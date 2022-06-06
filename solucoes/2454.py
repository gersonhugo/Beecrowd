e = input().split()
p = int(e[0])
r = int(e[1])

if p == 0:
    print('C')
elif p == 1:
    if r == 0:
        print('B')
    else:
        print('A')