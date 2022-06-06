i = input().split()
i1 = int(i[0])
i2 = int(i[1])
if i1 % i2 == 0 or i2 % i1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')