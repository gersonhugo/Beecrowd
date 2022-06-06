ei = input().split()
di = int(ei[1])
moi = input().split(' : ')
hi,mi,si = int(moi[0]), int(moi[1]), int(moi[2])

ef = input().split()
df = int(ef[1])
mof = input().split(' : ')
hf,mf,sf = int(mof[0]), int(mof[1]), int(mof[2])

w = df - di
x = hf - hi
y = mf - mi
z = sf - si

if z < 0:
    z+= 60
    y-= 1
if y < 0:
    y+= 60
    x-= 1
if x < 0:
    w -= 1
    x += 24

print('{} dia(s)'.format(w))
print('{} hora(s)'.format(x))
print('{} minuto(s)'.format(y))
print('{} segundo(s)'.format(z))