n = input().split()
e, f, c = int(n[0]), int(n[1]), int(n[2])

tomou = (e // c)
restou = (e % c)
vazias = f + tomou + restou

while not vazias < c:
    tomou += (vazias // c)
    restou = (vazias % c)
    vazias = (vazias // c) + restou

print(tomou)
