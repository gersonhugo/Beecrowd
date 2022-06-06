while True:
    s = 0
    x = int(input())
    if x == 0: break
    if x % 2 == 1:
        x+=1
    for i in range(x,x+10,2):
        s+=i
    print(s)