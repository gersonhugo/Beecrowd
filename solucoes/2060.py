n = int(input())
e = input().split()
l = []
for i in range(n):
    l.append(int(e[i]))

m2 = 0
m3 = 0
m4 = 0
m5 = 0

for i in l:
    if i % 2 == 0:
        m2 += 1
    if i % 3 == 0:
        m3 += 1
    if i % 4 == 0:
        m4 += 1
    if i % 5 == 0:
        m5 += 1

print(m2, 'Multiplo(s) de 2')
print(m3, 'Multiplo(s) de 3')
print(m4, 'Multiplo(s) de 4')
print(m5, 'Multiplo(s) de 5')