# Problema 1073 do Beecrowd - Quadrado de Pares

n = int(input())

for i in range(1, n+1):
    if i%2 == 0:
        print(f'{i}^2 = {i*i}')