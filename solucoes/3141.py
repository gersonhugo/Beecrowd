n = input()
a = input()
b = input()

if a[0:5] == b[0:5]:
    print('Feliz aniversario!')

aa = int(a[6:10]) - int(b[6:10])
mm = int(a[3:5]) - int(b[3:5])
dd = int(a[0:2]) - int(b[0:2])

if dd < 0:
    mm -= 1
if mm < 0:
    aa -= 1

print('Voce tem {} anos {}.'.format(aa, n))