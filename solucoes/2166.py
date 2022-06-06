n = int(input())

x = 0
for i in range(n):
    x += 2
    x = 1/x
x += 1

print("{:.10f}".format(x))
