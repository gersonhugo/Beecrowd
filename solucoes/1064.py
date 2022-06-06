pos = 0
som = 0
for i in range(6):
    v = float(input())
    if v > 0:
        pos += 1
        som += v
med = som / pos
print(pos, 'valores positivos')
print('{:.1f}'.format(med))