n = int(input())
s, b, a = 0, 0, 0
s1, b1, a1 = 0, 0, 0
for i in range(n):
    nome = input()

    e = input().split()
    s += int(e[0])
    b += int(e[1])
    a += int(e[2])

    e1 = input().split()
    s1 += int(e1[0])
    b1 += int(e1[1])
    a1 += int(e1[2])

s2 = s1*100/s
b2 = b1*100/b
a2 = a1*100/a

print('Pontos de Saque: {:.2f} %.'.format(s2))
print('Pontos de Bloqueio: {:.2f} %.'.format(b2))
print('Pontos de Ataque: {:.2f} %.'.format(a2))
