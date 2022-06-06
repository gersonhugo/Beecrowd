n = int(input())
for i in range(n):
    e = input()
    if e[0] == e[2]:
        print(int(e[0]) * int(e[2]))
    elif e[1].isupper():
        print(int(e[2]) - int(e[0]))
    else:
        print(int(e[0]) + int(e[2]))
