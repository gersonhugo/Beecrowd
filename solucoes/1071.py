x = int(input())
y = int(input())
s = 0
if x > y:
    for i in range(y+1, x):
        if i % 2 == 1:
            s += i
    print(s)
elif x < y:
    for i in range(x+1, y):
        if i % 2 == 1:
            s += i
    print(s)
else: print(0)