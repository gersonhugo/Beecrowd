n = int(input())
for i in range(n):
    e = input().split()
    h = int(e[0])
    d = int(e[1])
    g = int(e[2])
    if h >= 200 and h <= 300 and d >= 50 and g >= 150:
        print("Sim")
    else:
        print("Nao")
