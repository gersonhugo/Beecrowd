n = int(input())
l = [0,1]
for i in range(2, n):
        l.append(l[i-1]+l[i-2])
if n == 1:
    print(0)
elif n == 0:
    print()
else: print(*l)