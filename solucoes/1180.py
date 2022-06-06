n = int(input())
v = input().split()
m = int(v[0])
p = 0
for i in range(n):
    if int(v[i]) < m:
        m = int(v[i])
        p = i
print('Menor valor: {}'.format(m))
print('Posicao: {}'.format(p))