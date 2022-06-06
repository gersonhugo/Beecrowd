d = [(0,6),
     (1,2),
     (2,5),
     (3,5),
     (4,4),
     (5,5),
     (6,6),
     (7,3),
     (8,7),
     (9,6)]
n = int(input())
for i in range(n):
    s = 0
    v = str(input())
    for j in range(len(v)):
        s+= d[int(v[j])][1]
    print('{} leds'.format(s))