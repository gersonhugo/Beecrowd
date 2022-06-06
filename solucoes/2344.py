n = int(input())
if n == 0:
    print('E')
elif 0 < n < 36:
    print('D')
elif 35 < n < 61:
    print('C')
elif 60 < n < 86:
    print('B')
else:
    print('A')