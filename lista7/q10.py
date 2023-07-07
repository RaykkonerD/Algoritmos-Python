''' Dizemos que um n´umero natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4 × 5 × 6 = 120. Escreva um algoritmo que imprima os 10 primeiros números triangulares.'''


for i in range(10):
  print(i**3 + 3*i**2 + 2*i)


# print([(i**3 + 3*i**2 + 2*i) for i in range(10)])