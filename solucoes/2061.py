e = input().split()
n = int(e[0])
m = int(e[1])

for i in range(m):
    f = input()
    if f == "fechou":
        n += 1
    else:
        n -= 1
print(n)