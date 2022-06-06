while True:
    x = int(input())
    if x == 0:
        break
    l= []
    for x in range(1, x+1):
        l.append(x)
    print(*l)