e = input().split()
d1, d2, d3 = int(e[0]), int(e[1]), int(e[2])

# 1
if d1 > d2 <= d3:
    print(':)')

# 2
elif d1 < d2 >= d3:
    print(':(')

# 3
elif d1 < d2 < d3 and (d3 - d2) < (d2 - d1):
        print(':(')

# 4
elif d1 < d2 < d3 and (d3 - d2) >= (d2 - d1):
        print(':)')

# 5
elif d1 > d2 > d3 and (d2 - d3) < (d1 - d2):
        print(':)')

# 6
elif d1 > d2 > d3 and (d2 - d3) >= (d1 - d2):
        print(':(')

# 7
elif d1 == d2 < d3:
    print(':)')

# 8
elif d1 == d2 >= d3:
    print(':(')
