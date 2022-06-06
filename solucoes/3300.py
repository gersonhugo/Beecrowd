n = int(input())
s = str(n)
if s.count('13') > 0:
    print('{} es de Mala Suerte'.format(s))
else:
    print('{} NO es de Mala Suerte'.format(s))