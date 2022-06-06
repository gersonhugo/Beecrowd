while True:
    n = int(input())
    if n == 0:
        break
    m = 0
    j = 0
    e = input().split()
    for i in range(n):
        if e[i] == '0':
            m += 1
        else:
            j += 1
    print("Mary won {} times and John won {} times".format(m, j))
