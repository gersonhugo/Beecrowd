n = int(input())
l = [0,0,0]
s = 0
for i in range(n):
    e = input().split()
    if e[1] == 'C':
        l[0] += int(e[0])
    elif e[1] == 'R':
        l[1] += int(e[0])
    elif e[1] == 'S':
        l[2] += int(e[0])
s = l[0]+l[1]+l[2]
pc = 100 * l[0] / (l[0]+l[1]+l[2])
pr = 100 * l[1] / (l[0]+l[1]+l[2])
ps = 100 * l[2] / (l[0]+l[1]+l[2])

print('Total: {} cobaias'.format(s))
print('Total de coelhos: {}'.format(l[0]))
print('Total de ratos: {}'.format(l[1]))
print('Total de sapos: {}'.format(l[2]))
print('Percentual de coelhos: {:.2f} %'.format(pc))
print('Percentual de ratos: {:.2f} %'.format(pr))
print('Percentual de sapos: {:.2f} %'.format(ps))
