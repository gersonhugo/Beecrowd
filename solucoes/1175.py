n = []
for i in range(20):
    v = int(input())
    n.insert(0, v)
for j in range(20):
    print('N[{}] = {}'.format(j, n[j]))