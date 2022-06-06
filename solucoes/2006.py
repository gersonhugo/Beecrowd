t = int(input())
e = input().split()
s = 0
for c in e:
    if int(c) == t:
        s += 1
print(s)