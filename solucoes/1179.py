par = []
impar = []

for i in range(15):
    v = int(input())

    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

    if len(par) == 5:
        for i in range(len(par)):
            print('par[{}] = {}'.format(i,par[i]))
        par.clear()

    if len(impar) == 5:
        for i in range(len(impar)):
            print('impar[{}] = {}'.format(i, impar[i]))
        impar.clear()

for i in range(len(impar)):
    print('impar[{}] = {}'.format(i, impar[i]))

for i in range(len(par)):
    print('par[{}] = {}'.format(i, par[i]))
