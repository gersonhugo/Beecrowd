c = 0
k = 0
v = 0
n = int(input())
for i in range(n):
    c += 1
    v += float(input())
    e = input().split()
    k += len(e)
    print("day {}: {} kg".format(c, len(e)))
print("{:.2f} kg by day".format(k / c))
print("R$ {:.2f} by day".format(v / c))
