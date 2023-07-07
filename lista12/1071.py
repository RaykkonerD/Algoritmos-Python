# Problema 1071 do Beecrowd - Soma de Impares Consecutivos I

x = int(input())
y = int(input())
soma = 0

if y < x:
    temp = x
    x = y
    y = temp

for i in range(x+1, y):
    if i%2:
        soma += i

print(soma)