n = int(input())
for i in range(n):
    u = 0
    e = input()
    if len(e) == 3:
        if e[0] == 'o':
            u += 1
        if e[1] == 'n':
            u += 1
        if e[2] == 'e':
            u += 1

        if u >= 2:
            print('1')
        else:
            print('2')
    else:
        print('3')
