n = int(input())
for i in range(n):
    e = input().split()
    x = int(e[0])
    y = int(e[1])
    soma = 0
    for j in range(y):
        if x % 2 == 0:
            x += 1
        soma += x
        x += 2
    print(soma)