# Problema 1040 do Beecrowd - Média

n1, n2, n3, n4 = list(map(lambda a: float(a), input().split()))
media = (n1*2+n2*3+n3*4+n4*1)/10;

print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exameNota = float(input())
    print("Nota do exame: %.1f" % exameNota)
    media = (media + exameNota) / 2
    if media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")
    print("Media final: %.1f" % media)