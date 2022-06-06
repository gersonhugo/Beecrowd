en = "encaixa"
na = "nao encaixa"

n = int(input())

for i in range(n):
    e = input().split()
    a = e[0]
    b = e[1]
    if len(a) < len(b):
        print(na)
    elif b == a[-len(b):]:
        print(en)
    else:
        print(na)
