t = int(input())

for i in range(t):
    vb = int(input())

    e = input().split()
    a = int(e[0])
    d = int(e[1])
    l = int(e[2])
    b = 0

    e2 = input().split()
    a2 = int(e2[0])
    d2 = int(e2[1])
    l2 = int(e2[2])
    b2 = 0

    if l % 2 == 0:
        b = vb
    if l2 % 2 == 0:
        b2 = vb

    vg = (a + d) / 2 + b
    vg2 = (a2 + d2) / 2 + b2

    if vg > vg2:
        print("Dabriel")
    elif vg2 > vg:
        print("Guarte")
    else:
        print("Empate")
