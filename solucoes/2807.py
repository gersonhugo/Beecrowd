n = int(input())
a = 0
p = 1
l = [1]
for i in range(n-1):
    l.insert(0,a+p)
    a = p
    p = l[0]
print(*l)
