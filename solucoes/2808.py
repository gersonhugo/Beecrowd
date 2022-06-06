v = "VALIDO"
i = "INVALIDO"
e = input()
ci = ord(e[0])
cd = ord(e[3])
li = int(e[1])
ld = int(e[4])

if abs(ci - cd) == 2 and abs(li - ld) == 1 or abs(ci - cd) == 1 and abs(li - ld) == 2:
    print(v)
else:
    print(i)
