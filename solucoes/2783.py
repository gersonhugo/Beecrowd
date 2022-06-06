e = input().split()
fc = input().split()
f = input().split()

s = int(e[1])
for k in fc:
    for k2 in f:
        if k == k2:
            s -= 1
            break
print(s)
