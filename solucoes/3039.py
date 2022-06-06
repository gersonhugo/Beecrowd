n = int(input())
b = 0
c = 0
for i in range(n):
    e = input().split()
    l = e[1]

    if l == 'F':
        b +=1
    else:
        c +=1

print("{} carrinhos".format(c))
print("{} bonecas".format(b))