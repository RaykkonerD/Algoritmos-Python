'''Escreva um algoritmo que leia dois números, limite inferior e limite superior, some e imprima o quadrado, x², de todos os números de limite inferior a limite superior. Por exemplo, se o usuário digitar 2 como limite inferior e 5 como limite superior, deve imprimir 54.'''


li = int(input())
ls = int(input()) 
soma = 0

for i in range(li, ls+1):
  soma += i**2

print(soma)

# print(sum([i**2 for i in range(li, ls+1)]))