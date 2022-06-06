n = int(input())
s = 0
for i in range(n):
    e = input().split()
    p = (int(e[0][-1]) + 0.5) * int(e[1])
    s += p
print('{:.2f}'.format(s))