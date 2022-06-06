e = input().split()
l = int(e[0])
c = int(e[1])
m = []
x = 0
y = 0
for i in range(l):
    m.append(input().split())

for i in range(1, l - 1):
    for j in range(1, c - 1):
        if m[i][j] == '42':
            if m[i - 1][j - 1] == '7':
                if m[i - 1][j] == '7':
                    if m[i - 1][j + 1] == '7':
                        if m[i][j - 1] == '7':
                            if m[i][j + 1] == '7':
                                if m[i + 1][j - 1] == '7':
                                    if m[i + 1][j] == '7':
                                        if m[i + 1][j + 1] == '7':
                                            x = i + 1
                                            y = j + 1
print(x, y)
