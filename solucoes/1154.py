soma = 0
cont = 0
media = 0
while True:
    n = int(input())
    if n >= 0:
        soma += n
        cont += 1
        media = soma / cont
    else:
        print('{:.2f}'.format(media))
        break
