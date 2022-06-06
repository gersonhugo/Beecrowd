n = int(input())
for i in range(n):
    soma = 0
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])

    if x == y:
        print(0)

    if x < y:
        for i in range(x+1,y):
            if i % 2 == 1:
                soma += i
        print(soma)

    if y < x:
        for i in range(y+1,x):
            if i % 2 == 1:
                soma += i
        print(soma)
