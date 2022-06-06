e = input().split()
p = int(e[0])
n = int(e[1])
v = input().split()
for i in range(-n, -1, 1):
    if (int(v[i+1]) - int(v[i])) < -p:
        print('GAME OVER')
        break
    if p >= int(v[i+1]) - int(v[i]):
        if i == -2:
            print('YOU WIN')
    else:
        print('GAME OVER')
        break
