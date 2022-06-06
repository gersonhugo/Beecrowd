e = input().split()
a = int(e[0])
b = int(e[1])
c = int(e[2])

e2 = input().split()
a2 = int(e2[0])
b2 = int(e2[1])
c2 = int(e2[2])

s = 0

if a2 >= a:
    s += a2 - a
if b2 >= b:
    s += b2 - b
if c2 >= c:
    s += c2 - c

print(s)
