x = int(input())
s = 0
c = 0
while True:
    z = int(input())
    if z > x: break
for i in range(x, z):
    s += i
    c += 1
    if s > z:
        print(c)
        break