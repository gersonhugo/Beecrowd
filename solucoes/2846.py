k = int(input())

l = [0,1]
nl = []

for i in range(1, k+4):
    l.append(l[i]+l[i-1])

    for j in range(l[i]+1, l[i]+l[i-1]):
        nl.append(j)

    if len(nl) >= k:
        break

print(nl[k-1])
