n = int(input())
for i in range(n):
    e = input().split()
    if e[2] == '1':
        print("{:0>2}:{:0>2} - A porta abriu!".format(e[0], e[1]))
    else:
        print("{:0>2}:{:0>2} - A porta fechou!".format(e[0], e[1]))
