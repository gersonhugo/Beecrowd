v = int(input())

n100 = int(v / 100)
n50  = v % 100 // 50
n20  = v % 100 % 50 // 20
n10  = v % 100 % 50 % 20 // 10
n5   = v % 100 % 50 % 20 % 10 // 5
n2   = v % 100 % 50 % 20 % 10 % 5 // 2
n1   = v % 100 % 50 % 20 % 10 % 5 % 2 // 1

print(v)
print(n100,'nota(s) de R$ 100,00')
print(n50,'nota(s) de R$ 50,00')
print(n20,'nota(s) de R$ 20,00')
print(n10,'nota(s) de R$ 10,00')
print(n5,'nota(s) de R$ 5,00')
print(n2,'nota(s) de R$ 2,00')
print(n1,'nota(s) de R$ 1,00')
