n = input().split()
n1 = float(n[0])
n2 = float(n[1])
n3 = float(n[2])
n4 = float(n[3])
m = (n1*2 + n2*3 + n3*4 + n4) / 10
print('Media: {:.1f}'.format(m))
if m >= 7:
    print('Aluno aprovado.')
elif m < 5:
    print('Aluno reprovado.')
elif m >= 5 and m < 7:
    print('Aluno em exame.')
    e = float(input())
    print('Nota do exame: {:.1f}'.format(e))
    me = (e+m)/2
    if me >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(me))
    elif me < 5:
        print('Aluno reprovado.')