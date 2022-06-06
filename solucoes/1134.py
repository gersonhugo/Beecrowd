alc = 0
gas = 0
die = 0
while True:
    t = int(input())
    if t >= 1 or t <= 3:
        if t == 1:
            alc += 1
        elif t == 2:
            gas += 1
        elif t == 3:
            die += 1
    if t == 4:
        break
print('MUITO OBRIGADO')
print('Alcool:', alc)
print('Gasolina:', gas)
print('Diesel:', die)