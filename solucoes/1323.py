while True:
    n = int(input())
    if n == 0:
        break

    l = [0]
    for i in range(1, n+1):
        l.append(i ** 2 + l[i-1])
    print(l[n])
