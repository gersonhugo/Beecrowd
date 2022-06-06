input()
e = input().split()
for c in e:
    p = True
    n = int(c)
    if n < 2:
        p = False
    else:
        d = 2
        while d*d <= n:
            if n % d == 0:
                p = False
                break
            d+=1
    if p:
        f = n
        for i in range(n - 1, 1, -1):
            f *= i
        print('{}! = {}'.format(n, f))