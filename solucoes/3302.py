q = int(input())
n = []
for i in range(q):
    n.append(int(input()))
for i in range(1, len(n)+1):
    print('resposta {}: {}'.format(i, n[i-1]))