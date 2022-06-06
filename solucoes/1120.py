while True:
    e = input().split()
    if e[0] == "0" and e[1] == "0":
        break
    v = e[1].replace(e[0],'')
    if v == '':
        print(0)
    else:
        print(int(v))
