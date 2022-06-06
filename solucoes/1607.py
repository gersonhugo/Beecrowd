t = int(input())
for i in range(t):
    e = input().split()
    a = e[0]
    b = e[1]
    s = 0
    for j in range(len(a)):
        x = ord(b[j]) - ord(a[j])
        if x < 0:
            x += 26
        s += x
    print(s)
