n = int(input())
v = n
for i in range(n):
    e = input()
    for j in range(-1, -len(e), -1):
        if e[j] == 'D' and e[j-1] == 'C':
            v -= 1
print(v)