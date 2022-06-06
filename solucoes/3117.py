e = input().split()
n = int(e[0])
k = int(e[1])

h = input().split()

s = 0
for c in h:
    if int(c) <= 0:
        s += 1

if s < k:
    print('NO')
else:
    print('YES')
