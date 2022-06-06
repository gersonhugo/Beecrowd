maior = 0
pos = 0
for i in range(1,101):
    v = int(input())
    if v > maior:
        maior = v
        pos = i
print(maior)
print(pos)