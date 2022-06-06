while True:
    try:
        n = int(input())
        for i in range(n):
            e = input()
            if e == ".":
                print("a")
            elif e == "..":
                print("b")
            elif e == "...":
                print("c")
            elif e == ". .":
                print("d")
            elif e == ".. ..":
                print("e")
            elif e == "... ...":
                print("f")
            elif e == ". . .":
                print("g")
            elif e == ".. .. ..":
                print("h")
            elif e == "... ... ...":
                print("i")
            elif e == ". . . .":
                print("j")
            elif e == ".. .. .. ..":
                print("k")
            elif e == "... ... ... ...":
                print("l")
            elif e == ". . . . .":
                print("m")
            elif e == ".. .. .. .. ..":
                print("n")
            elif e == "... ... ... ... ...":
                print("o")
            elif e == ". . . . . .":
                print("p")
            elif e == ".. .. .. .. .. ..":
                print("q")
            elif e == "... ... ... ... ... ...":
                print("r")
            elif e == ". . . . . . .":
                print("s")
            elif e == ".. .. .. .. .. .. ..":
                print("t")
            elif e == "... ... ... ... ... ... ...":
                print("u")
            elif e == ". . . . . . . .":
                print("v")
            elif e == ".. .. .. .. .. .. .. ..":
                print("w")
            elif e == "... ... ... ... ... ... ... ...":
                print("x")
            elif e == ". . . . . . . . .":
                print("y")
            elif e == ".. .. .. .. .. .. .. .. ..":
                print("z")
    except EOFError:
        break
