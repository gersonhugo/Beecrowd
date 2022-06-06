t = int(input())
for i in range(t):
    c = input()
    v = input().split()
    r = int(v[0])
    g = int(v[1])
    b = int(v[2])

    if c == 'eye':
        p = int((0.3 * r) + (0.59 * g) + (0.11 * b))
        print('Caso #{}: {:.0f}'.format(i + 1, p))
    elif c == 'mean':
        p = int((r + g + b) / 3)
        print('Caso #{}: {:.0f}'.format(i + 1, p))
    elif c == 'max':
        p = max([r, g, b])
        print('Caso #{}: {:.0f}'.format(i + 1, p))
    elif c == 'min':
        p = min([r, g, b])
        print('Caso #{}: {:.0f}'.format(i + 1, p))
