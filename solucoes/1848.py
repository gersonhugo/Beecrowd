l = [0, 0, 0]
for i in range(3):
    v = 0
    while True:
        e = input()
        if e == '---':
            pass
        elif e == '--*':
            v += 1
        elif e == '-*-':
            v += 2
        elif e == '-**':
            v += 3
        elif e == '*--':
            v += 4
        elif e == '*-*':
            v += 5
        elif e == '**-':
            v += 6
        elif e == '***':
            v += 7
        elif e == 'caw caw':
            if v > 1000:
                v = 1000
            l[i] = v
            break
print(l[0])
print(l[1])
print(l[2])