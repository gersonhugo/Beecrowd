n = int(input())
e = input().split()
f = 0

for k in e:
    c = k
    while True:
        s = 0
        for j in c:
            s += int(j) * int(j)
        if s == 1 or s == 29 or s == 85 or s == 89 or s == 145 or s == 42 or s == 20 or s == 4:
            break
        c = str(s)
    if s == 1:
        f += 1
print(f)
