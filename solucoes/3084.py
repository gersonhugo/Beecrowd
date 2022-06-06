while True:
    try:
        e = input().split()
        h = int(int(e[0]) / 30)
        m = int(int(e[1]) / 6)
        print("{:0>2}:{:0>2}".format(h,m))
    except EOFError:
        break