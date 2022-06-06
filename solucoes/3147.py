ent = input().split()
h = int(ent[0])
e = int(ent[1])
a = int(ent[2])
o = int(ent[3])
w = int(ent[4])
x = int(ent[5])
bem = h + e + a
mal = o + w
if bem <= mal:
    bem += x
if bem >= mal:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')