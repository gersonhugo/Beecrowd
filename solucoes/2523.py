while True:
    try:
        s = input()
        n = int(input())
        l = input().split()
        m = []
        for i in range(n):
            m.append(s[int(l[i])-1])
        print(''.join(m))
    except EOFError: break