e = input().split()
p = int(e[0])
j1 = int(e[1])
j2 = int(e[2])
r = int(e[3])
a = int(e[4])
s = j1+j2
v1 = "Jogador 1 ganha!"
v2 = "Jogador 2 ganha!"

if r == 1 and a == 1:
    print(v2)
elif r == 1 and a == 0:
    print(v1)
elif r == 0 and a == 1:
    print(v1)
elif s % 2 == 0 and p == 1:
    print(v1)
elif s % 2 != 0 and p == 1:
    print(v2)
elif s % 2 != 0 and p == 0:
    print(v1)
elif s % 2 == 0 and p == 0:
    print(v2)
