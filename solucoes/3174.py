q = int(input())
bon = 0
arq = 0
mus = 0
des = 0
for i in range(q):
    dados = input().split()
    g = dados[1]
    h = int(dados[2])
    if g == 'bonecos':
        bon += h
    elif g == 'arquitetos':
        arq += h
    elif g == 'musicos':
        mus += h
    elif g == 'desenhistas':
        des += h
bon = int(bon / 8)
arq = int(arq / 4)
mus = int(mus / 6)
des = int(des / 12)
soma = bon + arq + mus + des
print(soma)