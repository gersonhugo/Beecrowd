e = input().split()
e[0] = int(e[0])
e[1] = int(e[1])
e[2] = int(e[2])

e.sort()

a = int(e[0])
b = int(e[1])
c = int(e[2])

if a + b <= c:
    print("Invalido")

elif a == b == c:
    print("Valido-Equilatero")
    print("Retangulo: N")

elif a == b or b == c:
    print("Valido-Isoceles")
    if a**2 + b**2 == c**2:
        print("Retangulo: S")
    else:
        print("Retangulo: N")

else:
    print("Valido-Escaleno")
    if a**2 + b**2 == c**2:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
