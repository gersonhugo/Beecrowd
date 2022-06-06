s = 0
c = 0
while True:
    try:
        input()
        d = int(input())
        s += d
        c += 1
    except EOFError:
        break
print("{:.1f}".format(s / c))
