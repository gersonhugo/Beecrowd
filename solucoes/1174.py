l = []
for i in range(100):
    v = float(input())
    if v <= 10:
        l.append((i, v))
for i in range(len(l)):
    print('A[{}] = {:.1f}'.format(l[i][0], l[i][1]))