n = int(input())
for i in range(n):
    x = int(input())

    if x == 0:
        print(0)
    else:
        x = bin(x)[2:]
        c = 1
        m = 1

        for j in range(len(x)-1):
            if x[j:j+2] == '11':
                c += 1
                if c > m:
                    m = c
            elif x[j] == '0':
                c = 1
        print(m)
