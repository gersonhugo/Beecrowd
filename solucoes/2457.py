c = input()
e = input().split()
s = 0
for k in e:
    if c in k:
        s += 1
print("{:.1f}".format(s*100/len(e)))
