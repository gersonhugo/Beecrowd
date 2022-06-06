a = "Os atributos dos monstros vao ser inteligencia, sabedoria..."
b = "Iron Maiden's gonna get you, no matter how far!"
c = "Urano perdeu algo muito precioso..."
e = "Putz vei, o Leo ta demorando muito pra jogar..."
while True:
    try:
        x = input()
        if x == "pedra pedra pedra":
            print(e)
        elif x == "pedra pedra papel":
            print(c)
        elif x == "pedra pedra tesoura":
            print(e)
        elif x == "pedra papel pedra":
            print(b)
        elif x == "pedra papel papel":
            print(e)
        elif x == "pedra papel tesoura":
            print(e)
        elif x == "pedra tesoura pedra":
            print(e)
        elif x == "pedra tesoura papel":
            print(e)
        elif x == "pedra tesoura tesoura":
            print(a)
        elif x == "papel pedra pedra":
            print(a)
        elif x == "papel pedra papel":
            print(e)
        elif x == "papel pedra tesoura":
            print(e)
        elif x == "papel papel pedra":
            print(e)
        elif x == "papel papel papel":
            print(e)
        elif x == "papel papel tesoura":
            print(c)
        elif x == "papel tesoura pedra":
            print(e)
        elif x == "papel tesoura papel":
            print(b)
        elif x == "papel tesoura tesoura":
            print(e)
        elif x == "tesoura pedra pedra":
            print(e)
        elif x == "tesoura pedra papel":
            print(e)
        elif x == "tesoura pedra tesoura":
            print(b)
        elif x == "tesoura papel pedra":
            print(e)
        elif x == "tesoura papel papel":
            print(a)
        elif x == "tesoura papel tesoura":
            print(e)
        elif x == "tesoura tesoura pedra":
            print(c)
        elif x == "tesoura tesoura papel":
            print(e)
        elif x == "tesoura tesoura tesoura":
            print(e)

    except EOFError:
        break
