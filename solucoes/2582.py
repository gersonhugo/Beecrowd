musicas =['PROXYCITY',
          'P.Y.N.G.',
          'DNSUEY!',
          'SERVERS',
          'HOST!',
          'CRIPTONIZE',
          'OFFLINE DAY',
          'SALT',
          'ANSWER!',
          'RAR?',
          'WIFI ANTENNAS']
c = int(input())
for i in range(c):
    n = input().split()
    print(musicas[ int(n[0]) + int(n[1])])