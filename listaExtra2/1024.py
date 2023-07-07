# Problema 1024 do Beecrowd - Criptografia

n = int(input())

for i in range(n):
  mensagem = input()
  encriptado = ""

  for caracter in mensagem:
    if caracter.isalpha():
      caracter = chr(ord(caracter) + 3)
    encriptado += caracter

  mensagem = encriptado[::-1]
  metade1 = mensagem[:len(mensagem) // 2]
  metade2 = mensagem[len(mensagem) // 2:]
  novaMetade = ""

  for caracter in metade2:
    caracter = chr(ord(caracter) - 1)
    novaMetade += caracter

  print(metade1 + novaMetade)