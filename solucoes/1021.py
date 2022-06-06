v = '{:.2f}'.format(float(input()))
s = v.split('.')
r = int(s[0])
c = int(s[1])

n100 = int(r / 100)
n50  = r % 100 // 50
n20  = r % 100 % 50 // 20
n10  = r % 100 % 50 % 20 // 10
n5   = r % 100 % 50 % 20 % 10 // 5
n2   = r % 100 % 50 % 20 % 10 % 5 // 2
m1   = r % 100 % 50 % 20 % 10 % 5 % 2 // 1
m050 = int(c / 50)
m025 = c % 50 // 25
m010 = c % 50 % 25 // 10
m005 = c % 50 % 25 % 10 // 5
m001 = c % 50 % 25 % 10 % 5 // 1

print('NOTAS:')
print(n100,'nota(s) de R$ 100.00')
print(n50,'nota(s) de R$ 50.00')
print(n20,'nota(s) de R$ 20.00')
print(n10,'nota(s) de R$ 10.00')
print(n5,'nota(s) de R$ 5.00')
print(n2,'nota(s) de R$ 2.00')
print('MOEDAS:')
print(m1,'moeda(s) de R$ 1.00')
print(m050, 'moeda(s) de R$ 0.50')
print(m025, 'moeda(s) de R$ 0.25')
print(m010, 'moeda(s) de R$ 0.10')
print(m005, 'moeda(s) de R$ 0.05')
print(m001, 'moeda(s) de R$ 0.01')
