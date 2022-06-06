e = input().split()
h = int(e[0])
z = int(e[1])
l = int(e[2])
if h < z < l or h > z > l:
    print('zezinho')
if h < l < z or h > l > z:
    print('luisinho')
if l < h < z or l > h > z:
    print('huguinho')
