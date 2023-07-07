# Problema 1045 do Beecrowd - Tipos de Triângulos

a, b, c = map(lambda a: float(a), input().split())

if a > b:
    if a > c:
        A = a
        B = c
        C = b
    else:
        A = c
        B = a
        C = b
else:
    if b > c:
        A = b
        B = c
        C = a
    else:
        A = c
        B = b
        C = a
    

if A >= B+C:
    print("NAO FORMA TRIANGULO")
elif (A*A) == (B*B)+(C*C):
    print("TRIANGULO RETANGULO")
elif (A*A) > (B*B)+(C*C):
    print("TRIANGULO OBTUSANGULO")
elif (A*A) < (B*B)+(C*C):
    print("TRIANGULO ACUTANGULO")

if A == B and B == C:
    print("TRIANGULO EQUILATERO");
elif A == C or B == C or A == B:
    print("TRIANGULO ISOSCELES")