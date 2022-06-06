while True:
    try:
        e = input().split()
        n = int(e[0])
        m = int(e[1])
        l = []
        for i in range(n):
            l.append(input().split())

        for i in range(n):
            for j in range(n):
                if l[i][j] == '1':
                    l[i][j] = '9'

        for k in l:
            print(''.join(k))
        print()

        for i in range(n):
            for j in range(n):
                print(i, j)
                s = 0
                if l[i][j] == '0':
                    if i == 0 and j == 0:
                        if l[i][j + 1] == '9':
                            s += 1
                        if l[i + 1][j] == '9':
                            s += 1
                    elif i == 0 and j != 0 and j < m-1:
                        if l[i][j - 1] == '9':
                            s += 1
                        if l[i][j + 1] == '9':
                            s += 1
                        if l[i + 1][j] == '9':
                            s += 1
                    else: i == 0

                    #
                    #
                    # if l[i - 1][j] == '9':
                    #     s += 1
                    # if l[i][j - 1] == '9':
                    #     s += 1
                    # if l[i][j + 1] == '9':
                    #     s += 1
                    # if l[i + 1][j] == '9':
                    #     s += 1
                    l[i][j] = str(s)
        for k in l:
            print(''.join(k))
    except EOFError:
        break
