while True:
    try:
        n = int(input())
        l = []
        for i in range(n*n):
            l.append('')
        for i in range(0,n*n,n+1):
            l[i] = '1'
        for i in range(n-1,n*n-1,n-1):
            l[i] = '2'
        for i in range(n*n):
            if l[i] == '':
                l[i] = '3'
        for i in range(0,n*n,n):
            print(''.join(l[i:i+n]))
    except EOFError: break