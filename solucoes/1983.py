n = int(input())
maior = 0
nota = 0
l = []
for i in range(n):
    e = input().split()
    l.append((int(e[0]), float(e[1])))

for t in l:
    if t[1] > nota:
        nota = t[1]
        maior = t[0]

if nota >= 8:
    print(maior)
else:
    print('Minimum note not reached')