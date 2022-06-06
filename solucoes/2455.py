e = input().split()
a = int(e[0])
b = int(e[1])
c = int(e[2])
d = int(e[3])

if a*b == c*d:
    print(0)
elif a*b < c*d:
    print(1)
else:
    print(-1)