t = int(input())
x = 0
for i in range(t):
    e = input().split()
    x += 1
    n = int(e[0])
    if n % 2 == 0:
        idd = e[int(n / 2 + 1)]
    else:
        idd = e[int((n+1) / 2)]
    print("Case {}: {}".format(x, idd))
