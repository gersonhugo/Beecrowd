t = int(input())
for i in range(t):
    e = input().split()
    pa, pb, ga, gb = int(e[0]), int(e[1]), float(e[2]), float(e[3])
    a, b = pa, pb
    an = 0
    while a <= b:
        a += int(a * (ga/100))
        b += int(b * (gb/100))
        an += 1
        if an > 100: break
    if an <= 100:
        print('{} anos.'.format(an))
    else:
        print('Mais de 1 seculo.')