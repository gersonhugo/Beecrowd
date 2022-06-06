e1 = input().split()
e2 = input().split()
e3 = input().split()
e4 = input().split()

s1 = 0
s2 = 0
s3 = 0
s4 = 0

m = 0

for i in e1:
    s1 += int(i)

for i in e2:
    s2 += int(i)

for i in e3:
    s3 += int(i)

for i in e4:
    s4 += int(i)

m = max(s1, s2, s3, s4)
print('{} = {}'.format(m, bin(m)[2:]))