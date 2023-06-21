# Problema 1044 do Beecrowd - Múltiplos

linha = input().split();
A = int(linha[0])
B = int(linha[1])

if (B % A) == 0 or (A % B) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")