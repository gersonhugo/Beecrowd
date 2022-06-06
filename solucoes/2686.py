import struct
from math import floor, ceil
while True:
    try:
        f = float(input())
        # print(f)

        if f >= 0 and f <= 89.9:
            print("Bom Dia!!")
        elif f >= 90 and f <= 179.9:
            print("Boa Tarde!!")
        elif f >= 180 and f <= 269.9:
            print("Boa Noite!!")
        elif f >= 270 and f <= 359.9:
            print("De Madrugada!!")
        elif f == 360:
            print("Bom Dia!!")

        # f += 90
        # if f >= 360:
        #     f = f % 360

        f = struct.unpack('f', struct.pack('f', f))[0]

        t = (240 * f) + 21600
        # print('t', t)
        if t >= 86400:
            t -= 86400
        # print('t2', t)

        h = int(t / 3600)
        # print('h', h)

        m = int(t % 3600 / 60)
        # print('m', m)

        s = int(round(t % 3600 % 60, 1))
        # print(s)

        print('{:0>2d}:{:0>2d}:{:0>2d}'.format(h, m, s))

    except EOFError:
        break
