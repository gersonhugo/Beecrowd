l = []
while True:
    try:
        e = input()
        if e[:1] == '(' or e[:1] == ')':
            if not e in l:
                l.append(e)
    except EOFError:
        break
print(len(l))
