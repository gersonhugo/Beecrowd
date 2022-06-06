n = int(input())
m = int(input())
l = []
for i in range(1, n+1):
    l.append(i)

for i in range(m):
    e = int(input())
    if e in l:
        l.remove(e)

print(len(l))
