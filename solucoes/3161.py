e = input().split()
n = int(e[0])
m = int(e[1])
f = []
e = []
for i in range(n):
    f.append(input().lower())
for i in range(m):
    e.append(input().lower())
s = ''.join(e)
for i in range(n):
    x = s.count(f[i])
    y = s.count(f[i][::-1])
    if x > 0 or y >0:
        print('Sheldon come a fruta {}'.format(f[i]))
    else:
        print("Sheldon detesta a fruta {}".format(f[i]))