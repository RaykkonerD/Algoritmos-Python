palavra = input("Digite uma palavra: ").lower()
invertida = ''

for letra in palavra:
  invertida = letra + invertida

print(f'{palavra} é um palíndromo!' if palavra == invertida else f'{palavra} não é um palíndromo!')
