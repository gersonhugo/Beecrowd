while True:
    try:
        e = input().split()
        m, n = int(e[0]), int(e[1])
        fm = 1
        fn = 1
        for i in range(1,m+1):
            fm *= i
        for i in range(1, n+1):
            fn *= i
        print(fm+fn)
    except EOFError: break