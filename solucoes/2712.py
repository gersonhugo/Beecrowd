f = "FAILURE"
n = int(input())
for i in range(n):
    e = input()
    if len(e) != 8:
        print(f)
    elif e[3] != '-':
        print(f)
    elif not (e[:3].isalpha() and e[:3].isupper()):
        print(f)
    elif not e[4:8].isnumeric():
        print(f)
    elif e[7] == '1' or e[7] == '2':
        print("MONDAY")
    elif e[7] == '3' or e[7] == '4':
        print("TUESDAY")
    elif e[7] == '5' or e[7] == '6':
        print("WEDNESDAY")
    elif e[7] == '7' or e[7] == '8':
        print("THURSDAY")
    elif e[7] == '9' or e[7] == '0':
        print("FRIDAY")
