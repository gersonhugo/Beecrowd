par = 0
for i in range(5):
    v = int(input())
    if v % 2 == 0:
        par += 1
print(par, 'valores pares')