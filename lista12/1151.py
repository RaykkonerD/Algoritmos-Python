# Problema 1151 do Beecrowd -	Fibonacci Fácil

n = int(input())
antes = 0
atual = 1
stringFinal = '0 1'

for i in range(n - 2):
  soma = antes + atual
  antes = atual
  atual = soma
  stringFinal += ' ' + str(atual)
    
print(stringFinal)