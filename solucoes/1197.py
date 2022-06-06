while True:
    try:
        e = input().split()
        print(int(e[0]) * int(e[1]) * 2)
    except EOFError:
        break
