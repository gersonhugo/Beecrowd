e = input().split()
s, t, f = int(e[0]), int(e[1]), int(e[2])
c = s + t
h = c +f
if h > 24: h -= 24
if h < 0: h += 24
if h == 24: h = 0
print(h)