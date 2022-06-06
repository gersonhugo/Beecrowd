# -*- coding: utf-8 -*-

ddd = int(input())
dic = [(61, 'Brasilia'),
       (71, 'Salvador'),
       (11, 'Sao Paulo'),
       (21, 'Rio de Janeiro'),
       (32, 'Juiz de Fora'),
       (19, 'Campinas'),
       (27, 'Vitoria'),
       (31, 'Belo Horizonte')]

achou = False
for i in range(len(dic)):
    if ddd == dic[i][0]:
        achou = True
        print(dic[i][1])
if achou == False:
    print('DDD nao cadastrado')