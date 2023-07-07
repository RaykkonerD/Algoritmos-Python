num = int(input("Digite um número inteiro: "))

if num == 1:
  print("1 não é primo!")
  
divisor = num - 1
divisao = num%divisor
  
while divisao:
  divisor -= 1
  divisao = num%divisor

if divisor == 1:
  print(f"{num} é primo!")
else:
  print(f"{num} não é primo! É divisível por, pelo menos, {divisor}.")