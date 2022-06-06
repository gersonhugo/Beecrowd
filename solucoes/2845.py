n = int(input())
e = input().split()
m = 0
for k in e:
    if int(k) > m:
        m = int(k)
print(m+1)
