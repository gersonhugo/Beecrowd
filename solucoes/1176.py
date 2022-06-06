t = int(input())
for i in range(t):
    n = int(input())
    l = [0,1]
    if n == 1:
        f = 1
        print('Fib({}) = {}'.format(n, f))
    elif n == 0:
        f = 0
        print('Fib({}) = {}'.format(n, f))
    else:
        for j in range(2, n+1):
            f = l[j-1]+l[j-2]
            l.append(f)
        print('Fib({}) = {}'.format(n, f))
        l = [0,1]