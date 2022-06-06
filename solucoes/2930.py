x = input().split()
e = int(x[0])
d = int(x[1])
if e > d:
    print("Eu odeio a professora!")
elif d - e >= 3:
    print("Muito bem! Apresenta antes do Natal!")
elif d - e <= 2:
    print("Parece o trabalho do meu filho!")
    if e + 2 < 24:
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")
