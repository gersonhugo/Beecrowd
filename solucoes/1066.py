par = 0
impar = 0
pos = 0
neg = 0
for i in range(5):
    v = int(input())
    if v % 2 == 0:
        par += 1
    else:
        impar += 1
    if v > 0:
        pos += 1
    if v < 0:
        neg += 1
print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(pos, 'valor(es) positivo(s)')
print(neg, 'valor(es) negativo(s)')