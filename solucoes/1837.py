e = input().split()
a = int(e[0])
b = int(e[1])
q = int(a / b)
r = - b * q + a

def modulo(x):
    if x < 0:
        x*= -1
    return x

while r < 0 or r >= modulo(b):
    if a / b < 0:
        q -= 1
    else: q += 1
    r =  - b * q + a

print(q, r)