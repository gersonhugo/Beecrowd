e = input()
c = 0

for i in range(len(e)):
    if e[i] == '1':
        c += 1

if c % 2 == 0:
    print(e + '0')
else:
    print(e + '1')
