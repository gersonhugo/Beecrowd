n = int(input())
for i in range(n):
    t = int(input())
    a = 2015 - t
    if a <= 0:
        a = a * -1 + 1
        print('{} A.C.'.format(a))
    else:
        print('{} D.C.'.format(a))