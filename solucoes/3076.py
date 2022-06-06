while True:
    try:
        n = int(input())
        s = n
        s += 99
        s = int(s/100)
        print(s)
    except EOFError:
        break