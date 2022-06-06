n = int(input())
e = input().split()
l = []
mv = int(e[0])
mi = 1
for i in range(n):
    l.append(int(e[i]))

for i in range(n):
    if l[i] < mv:
        mv = l[i]
        mi = i+1

print(mi)