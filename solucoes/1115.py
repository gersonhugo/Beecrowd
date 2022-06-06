while True:
    c = input().split()
    x = int(c[0])
    y = int(c[1])
    if x > 0 and y > 0:
        print('primeiro')
    elif x > 0 and y < 0:
        print('quarto')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x < 0 and y > 0:
        print('segundo')
    else: break