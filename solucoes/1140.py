while True:
    e = input()
    if e == "*":
        break

    e = e.split()

    r = "Y"
    for i in range(len(e)-1):
        if e[i][0].lower() != e[i+1][0].lower():
            r = 'N'
            break

    print(r)
