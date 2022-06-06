a = 3
b = 0
n = int(input())
for i in range(4, n + 1):
    b = b + a - 1
    a = i
print(b)
