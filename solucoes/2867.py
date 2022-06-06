c = int(input())
for i in range(c):
    e = input().split()
    n = int(e[0])
    m = int(e[1])
    p = n ** m
    print(len(str(p)))
