q = int(input())
for i in range(q):
    e = input().split()
    for j in range(len(e)):
        e[j] = int(e[j])

    soma = 0
    for k in range(1, len(e)):
        soma += e[k]
    m = soma - e[0] + 1
    print(m)