'''Escreva um algoritmo que leia 10 números inteiros e imprima, a soma deles.'''


soma = 0

for i in range(10):
  soma += float(input())

print('SOMA = %f' % soma)

# print(sum([float(input()) for i in range(10)]))