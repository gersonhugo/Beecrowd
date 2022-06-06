n = int(input())
la, lb = input().split()
sa, sb = input().split()
if n >= int(la) and n <= int(lb) and n >= int(sa) and n <= int(sb):
    print("possivel")
else:
    print("impossivel")
