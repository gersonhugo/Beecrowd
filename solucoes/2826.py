a = input()
b = input()
c = False

if len(a) < len(b):
    me = a
    ma = b
else:
    me = b
    ma = a

for i in range(len(me)):
    if ord(a[i]) < ord(b[i]):
        c = True
        print(a)
        print(b)
        break
    elif ord(b[i]) < ord(a[i]):
        c = True
        print(b)
        print(a)
        break

if a == b:
    print(a)
    print(b)
elif not c:
    print(me)
    print(ma)
