while True:
    try:
        e = input().split()
        c = int(e[0])
        n = int(e[1])
        s = input()
        o = input()
        for i in range(n):
            e = input()
            l = []
            for k in e:
                l += k
            for i in range(len(l)):
                for j in range(c):
                    if str(l[i]).lower() == o[j].lower():
                        if str(l[i]).isupper():
                            l[i]= s[j]
                        else:
                            l[i] = s[j].lower()
                    elif str(l[i]).lower() == s[j].lower():
                        if str(l[i]).isupper():
                            l[i]= o[j]
                        else:
                            l[i] = o[j].lower()
            print(''.join(l))
        print()

    except EOFError:
        break
