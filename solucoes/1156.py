s = 1
r = 1
for i in range(1,39,2):
    s+= (i+2)/(r*2)
    r*=2
print('{:.2f}'.format(s))