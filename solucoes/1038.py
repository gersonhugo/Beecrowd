i = input().split()
c = int(i[0])
q = int(i[1])
if c == 1:
    t = 4 * q
    print('Total: R$ {:.2f}'.format(t))
elif c == 2:
    t = 4.5 * q
    print('Total: R$ {:.2f}'.format(t))
elif c == 3:
    t = 5 * q
    print('Total: R$ {:.2f}'.format(t))
elif c == 4:
    t = 2 * q
    print('Total: R$ {:.2f}'.format(t))
elif c == 5:
    t = 1.5 * q
    print('Total: R$ {:.2f}'.format(t))
