n = int(input())
l = []
for i in range(n):
    if i == (n-1):
        l.append('Ho!')
    else: l.append('Ho')
print(*l)