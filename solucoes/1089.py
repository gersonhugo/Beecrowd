while True:
    n = int(input())
    if n == 0:
        break
    p = 0
    me = 0
    ma = 0
    e = input().split()
    if int(e[1]) < int(e[0]):
        p += 1
        v = 'd'
    elif int(e[1]) > int(e[0]):
        p += 1
        v = 's'

    for i in range(1, len(e)-1):
            print(e[i])
            if v == 'd':

    if v == 'd' and int(e[0]) > int(e[-1]):
        p +=1
    elif v == 's' and int(e[0]) < int(e[-1]):
        p +=1
    eli

        # if int(k) < me:
            #     me = int(k)
            #     p += 1
            # elif int(k) > ma:
            #     ma = int(k)
            #     p += 1
    print(p)
