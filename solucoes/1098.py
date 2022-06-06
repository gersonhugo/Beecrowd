i = 0
j = 1
while True:
    if str(int(j)*1.0) == '{:.1f}'.format(j):
        print('I={:.0f} J={:.0f}'.format(i,j))
        j += 1
        print('I={:.0f} J={:.0f}'.format(i, j))
        j += 1
        print('I={:.0f} J={:.0f}'.format(i, j))
    else:
        print('I={:.1f} J={:.1f}'.format(i,j))
        j += 1
        print('I={:.1f} J={:.1f}'.format(i, j))
        j += 1
        print('I={:.1f} J={:.1f}'.format(i, j))
    j -= 2
    j += 0.2
    i += 0.2
    if i > 2:
        break