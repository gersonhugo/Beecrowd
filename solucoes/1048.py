s = float(input())
if s >0 and s <= 400.00:
    r = s*15/100
    ns = s + r
    p = 15
if s >= 400.01 and s <= 800.00:
    r = s * 12 / 100
    ns = s + r
    p = 12
if s >= 800.01 and s <= 1200.00:
    r = s * 10 / 100
    ns = s + r
    p = 10
if s >= 1200.01 and s <= 2000.00:
    r = s * 7 / 100
    ns = s + r
    p = 7
if s > 2000.00:
    r = s * 4 / 100
    ns = s + r
    p = 4
print('Novo salario: {:.2f}'.format(ns))
print('Reajuste ganho: {:.2f}'.format(r))
print('Em percentual: {:.0f} %'.format(p))