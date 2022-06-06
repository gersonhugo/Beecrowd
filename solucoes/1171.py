n = int(input())
l =[]
for i in range(n):
    e = int(input())
    l.append(e)
l = sorted(l)
nl = []
for i in range(len(l)):
    if not l[i] in nl:
        print('{} aparece {} vez(es)'.format(l[i], l.count(l[i])))
        nl.append(l[i])