n = int(input())
k = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l.sort(reverse=True)

s = k
for i in range(k, len(l)):
    if l[k-1] == l[i]:
        s += 1
    else:
        break

print(s)
