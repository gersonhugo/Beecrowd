n = int(input())
e = input().split()
a = False
for i in range(n-1):
    if int(e[i+1]) < int(e[i]):
        print(i+2)
        a = True
        break
if not a:
    print(0)
