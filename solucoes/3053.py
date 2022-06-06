n = int(input())
p = input()
l = ["A", "B", "C"]

for i in range(n):
    m = int(input())

    if m == 1:
        copo = l[1]
        l.pop(1)
        l.insert(0,copo)
    elif m == 2:
        copo = l[2]
        l.pop(2)
        l.insert(1, copo)
    else:
        copo = l[2]
        cop2 = l[0]
        l.pop(2)
        l.insert(0, copo)
        l.pop(1)
        l.insert(2, cop2)

if l.index(p) == 0:
    print("A")
elif l.index(p) == 1:
    print("B")
else:
    print("C")