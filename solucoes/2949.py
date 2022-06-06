n = int(input())
a = 0
e = 0
h = 0
m = 0
x = 0
for i in range(n):
    n, r = input().split()
    if r == 'A':
        a+= 1
    elif r == 'E':
        e+= 1
    elif r == 'H':
        h += 1
    elif r == 'M':
        m +=1
    else:
        x += 1
print("{} Hobbit(s)".format(x))
print("{} Humano(s)".format(h))
print("{} Elfo(s)".format(e))
print("{} Anao(s)".format(a))
print("{} Mago(s)".format(m))
