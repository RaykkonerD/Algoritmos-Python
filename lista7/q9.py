'''Escreva um algoritmo que leia uma palavra e indique o número de ocorrências da letra A.'''


texto = input().upper()
cont = 0

for c in texto:
  if c == 'A':
    cont += 1

print('"A" aparece %d vezes.' % cont)

# print(texto.count('A'))