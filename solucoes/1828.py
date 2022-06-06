n = int(input())
for t in range(1, n+1):
    e = input().split()
    sh, ra = e[0], e[1]
    r1 = 'Bazinga!'
    r2 = 'Raj trapaceou!'
    r3 = 'De novo!'
    r = ''

    # 0
    if sh == ra:
        r = r3
    # 1
    elif sh == 'tesoura' and ra == 'papel':
        r = r1
    elif ra == 'tesoura' and sh == 'papel':
        r = r2

    # 2
    elif sh == 'papel' and ra == 'pedra':
        r = r1
    elif ra == 'papel' and sh == 'pedra':
        r = r2

    # 3
    elif sh == 'pedra' and ra == 'lagarto':
        r = r1
    elif ra == 'pedra' and sh == 'lagarto':
        r = r2

    # 4
    elif sh == 'lagarto' and ra == 'Spock':
        r = r1
    elif ra == 'lagarto' and sh == 'Spock':
        r = r2

    # 5
    elif sh == 'Spock' and ra == 'tesoura':
        r = r1
    elif ra == 'Spock' and sh == 'tesoura':
        r = r2

    # 6
    elif sh == 'tesoura' and ra == 'lagarto':
        r = r1
    elif ra == 'tesoura' and sh == 'lagarto':
        r = r2

    # 7
    elif sh == 'lagarto' and ra == 'papel':
        r = r1
    elif ra == 'lagarto' and sh == 'papel':
        r = r2

    # 8
    elif sh == 'papel' and ra == 'Spock':
        r = r1
    elif ra == 'papel' and sh == 'Spock':
        r = r2

    # 9
    elif sh == 'Spock' and ra == 'pedra':
        r = r1
    elif ra == 'Spock' and sh == 'pedra':
        r = r2

    # 10
    elif sh == 'pedra' and ra == 'tesoura':
        r = r1
    elif ra == 'pedra' and sh == 'tesoura':
        r = r2

    print('Caso #{}: {}'.format(t, r))