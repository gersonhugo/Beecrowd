t = 0
j = 0
while True:
    e = input()
    if e[:5] == "ABEND":
        break
    if e[:6] == "SALIDA":
        t+= int(e[7:9])
        j += 1
    elif e[:6] == "VUELTA":
        t -= int(e[7:9])
        j -= 1
print(t)
print(j)
