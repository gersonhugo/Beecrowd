n = int(input())
l = []

for i in range(n):
    e = input().split()
    p = float(e[0])
    g = int(e[1])
    b = 1000 / g * p
    l.append(b)

print("{:.2f}".format(min(l)))