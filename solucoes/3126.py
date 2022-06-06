c = int(input())
e = input().split()
s = 0
for i in range(c):
    if int(e[i]) == 1:
        s += 1
print(s)