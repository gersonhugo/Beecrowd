while True:
    n = int(input())
    if n == 0:
        break
    r = []
    d = []
    for i in range(1, n + 1):
        r.append(' ' + str(i))
    while len(r) > 1:
        for k in r:
            d.append(k)
            r.remove(k)
            r.append(r[0])
            r.pop(0)
            break
    print("Discarded cards:{}".format(','.join(d)))
    print("Remaining card:{}".format(','.join(r)))
