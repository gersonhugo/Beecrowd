i = 1
j = 7
while True:
    print('I={} J={}'.format(i,j))
    j -= 1
    print('I={} J={}'.format(i, j))
    j -= 1
    print('I={} J={}'.format(i, j))
    j += 4
    i += 2
    if i == 11:
        break