while True:
    try:
        m = int(input())
        if m >= 0 and m <= 89:
            print("Bom Dia!!")
        elif m >= 90 and m <= 179:
            print("Boa Tarde!!")
        elif m >= 180 and m <= 269:
            print("Boa Noite!!")
        elif m >= 270 and m <= 359:
            print("De Madrugada!!")
        elif m == 360:
            print("Bom Dia!!")
    except EOFError:
        break
