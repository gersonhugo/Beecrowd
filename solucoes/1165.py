n = int(input())
for i in range(n):
    p = True
    x = int(input())
    for j in range(x-1,1,-1):
        if x % j == 0:
            p = False
            break
    if p: print('{} eh primo'.format(x))
    else: print('{} nao eh primo'.format(x))