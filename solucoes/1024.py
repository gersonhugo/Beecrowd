from math import ceil

n = int(input())
for i in range(n):
    e = input()
    a1 = []
    a2 = []

    for j in e:
        if j.isalpha():
            a1.append(chr(ord(j)+3))
        else : a1.append(j)

    for k in range(-1, -len(e)-1, -1):
        a2.append(a1[k])

    a3 = a2
    for l in range(-1, int(-ceil(len(a2)/2))-1, -1):
        a3[l] = chr(ord(a2[l]) - 1)

    print(''.join(a3))