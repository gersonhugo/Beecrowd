while True:
    e = input().split()
    if int(e[0]) == 0 and int(e[1]) == 0:
        break

    print(str(int(e[0]) + int(e[1])).replace('0',''))
