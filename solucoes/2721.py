r = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]
e = input().split()

s = 0
for k in e:
    s += int(k)

print(r[s % 9 - 1])
