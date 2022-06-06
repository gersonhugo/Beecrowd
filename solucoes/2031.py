n = int(input())
pe = "pedra"
pa = "papel"
at = "ataque"
v1 = "Jogador 1 venceu"
v2 = "Jogador 2 venceu"
ab = "Ambos venceram"
sg = "Sem ganhador"

for i in range(n):
    a = input()
    b = input()
    if a == at and b == pe:
        print(v1)
    elif b == at and a == pe:
        print(v2)
    elif a == pe and b == pa:
        print(v1)
    elif b == pe and a == pa:
        print(v2)
    elif a == at and b == pa:
        print(v1)
    elif b == at and a == pa:
        print(v2)
    elif a == pa and b == pa:
        print(ab)
    elif a == pe and b == pe:
        print(sg)
    else:
        print("Aniquilacao mutua")
