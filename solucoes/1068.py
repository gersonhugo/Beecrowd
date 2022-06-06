c = "correct"
i = "incorrect"
while True:
    try:
        e = input()
        if e == '':
            print(c)
        else:
            l = []
            for j in range(len(e)):
                if e[j] == '(' or e[j] == ')':
                    l.append(e[j])

            if len(l) == 0:
                print(c)
            elif len(l) == 1:
                print(i)
            else:

                j = 0
                while True:
                    if l[j] == '(' and l[j + 1] == ')':
                        l.pop(j)
                        l.pop(j)
                        if len(l) == 0 or len(l) == 1:
                            break
                        if j > 0:
                            j = 0
                    else:
                        j += 1

                    if j == len(l) - 1:
                        break

                if len(l) == 0:
                    print(c)
                else:
                    print(i)

    except EOFError:
        break
