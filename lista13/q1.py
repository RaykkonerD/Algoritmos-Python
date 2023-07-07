# Funções

def maior(lista):
  maior = None 
  for n in lista:
    if maior == None or n > maior:
      maior = n 
  return maior
  
def menor(lista):
  menor = None 
  for n in lista:
    if menor == None or n < menor:
      menor = n 
  return menor

def soma(lista):
  soma = 0
  for n in lista:
    soma += n 
  return soma

# Leitura

numeros = []

for i in range(3):
  numeros.append(int(input())) 

# Saída 

print('Maior:', maior(numeros))
print('Menor:', menor(numeros))
print('Soma:', soma(numeros))