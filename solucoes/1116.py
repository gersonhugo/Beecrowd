n = int(input())
for i in range(n):
    v = input().split()
    x = int(v[0])
    y = int(v[1])
    if y == 0:
        print('divisao impossivel')
    else:
        d = x / y
        print('{:.1f}'.format(d))