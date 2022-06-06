a = input().split()
b = input().split()
p = "Y"
for i in range(5):
    if int(a[i]) == int(b[i]):
        p = "N"
        break
print(p)
