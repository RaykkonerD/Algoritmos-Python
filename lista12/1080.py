# Problema 1080 do Beecrowd - Maior e Posição

maior = None
posicao = None

for i in range(1, 101):
    n = int(input())
    if maior == None or  n > maior:
        maior = n
        posicao = i
        
print(maior)
print(posicao)