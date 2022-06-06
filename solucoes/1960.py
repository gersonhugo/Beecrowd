n = int(input())

c = [ "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
d = [ "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
u = [ "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]
l = []

i = int(n / 100)
r = n % 100

if i == 1:
    l += c[0]
elif i == 2:
    l += c[1]
elif i == 3:
    l += c[2]
elif i == 4:
    l += c[3]
elif i == 5:
    l += c[4]
elif i == 6:
    l += c[5]
elif i == 7:
    l += c[6]
elif i == 8:
    l += c[7]
elif i == 9:
    l += c[8]

i = int(r / 10)
r = n % 10

if i == 1:
    l += d[0]
elif i == 2:
    l += d[1]
elif i == 3:
    l += d[2]
elif i == 4:
    l += d[3]
elif i == 5:
    l += d[4]
elif i == 6:
    l += d[5]
elif i == 7:
    l += d[6]
elif i == 8:
    l += d[7]
elif i == 9:
    l += d[8]

i = r

if i == 1:
    l += u[0]
elif i == 2:
    l += u[1]
elif i == 3:
    l += u[2]
elif i == 4:
    l += u[3]
elif i == 5:
    l += u[4]
elif i == 6:
    l += u[5]
elif i == 7:
    l += u[6]
elif i == 8:
    l += u[7]
elif i == 9:
    l += u[8]

print(''.join(l))
