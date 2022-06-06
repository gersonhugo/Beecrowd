n = int(input())
l = []
for i in range(n):
    v = input().split()
    m = (float(v[0]) * 2 + float(v[1]) * 3 + float(v[2]) * 5) / 10
    print('{:.1f}'.format(m))