i = 1
j = 7
while True:
    print('I={} J={}'.format(i,j))
    j = 6
    print('I={} J={}'.format(i, j))
    j = 5
    print('I={} J={}'.format(i, j))
    j = 7
    i += 2
    if i == 11:
        break