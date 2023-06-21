'''Um número par é um número inteiro que pode ser escrito na forma 2n e n é inteiro. Escreva um algoritmo que escreva a soma dos 100 números pares consecutivos, iniciando do 100.'''


soma = 0

for i in range(100, 300, 2):
  soma += i 

print(soma)

# print(sum([i for i in range(100, 300, 2)]))