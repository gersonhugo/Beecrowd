n = int(input())
e = input()
if n < 3:
    print(1)
else:
    e = e.split()
    c = 1
    d = int(e[1]) - int(e[0])

    for i in range(1, n-1):
        if int(e[i+1]) - int(e[i]) != d:
            c += 1
            d = int(e[i + 1]) - int(e[i])
    print(c)
