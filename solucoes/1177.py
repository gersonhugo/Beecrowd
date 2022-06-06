t = int(input())
n = 0
while True:
    for i in range(0,t):
        print('N[{}] = {}'.format(n,i))
        n+= 1
        if n > 999:
            break
    if n > 999:
        break