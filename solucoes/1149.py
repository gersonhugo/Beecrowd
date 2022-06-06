e = input().split()
s = 0
a = int(e[0])
for i in range(1, len(e)):
    for j in range(0,int(e[i])):
        s+= (a+j)
print(s)