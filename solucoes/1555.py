n = int(input())
for i in range(n):
    e = input().split()
    x = int(e[0])
    y = int(e[1])

    r = (3 * x) ** 2 + y ** 2
    b = 2 * x ** 2 + (5 * y) ** 2
    c = -100 * x + y ** 3

    if c > b and c > r:
        print("Carlos ganhou")
    elif b > r and b > c:
        print("Beto ganhou")
    elif r > b and r > c:
        print("Rafael ganhou")
