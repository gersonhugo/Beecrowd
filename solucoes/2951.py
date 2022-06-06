e = input().split()
n = int(e[0])
g = int(e[1])
l = []
for i in range(n):
    e = input().split()
    l.append((e[0], int(e[1])))
x = int(input())
u = input().split()

s = 0
for i in range(x):
    for j in range(n):
        if u[i] == l[j][0]:
            s += l[j][1]
print(s)
if s < g:
    print("My precioooous")
else:
    print("You shall pass!")
