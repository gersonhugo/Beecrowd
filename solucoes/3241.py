# -*- coding: utf-8 -*-

n = int(input())
for i in range(n):
    e = input()
    if '+' in e:
        l = e.split('+')
        print(int(l[0])+int(l[1]))
    else:
        print('skipped')