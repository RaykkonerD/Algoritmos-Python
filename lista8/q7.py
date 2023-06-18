sequencia = input('Insira a sequência de resultados: ')
pontuacao = 0

for resultado in sequencia:
  if resultado == 'V':
    pontuacao += 3
  elif resultado == 'E':
    pontuacao += 1

print(f'Pontuação: {pontuacao}')

# pontuacao = sequencia.count('V')*3 + sequencia.count('E')
# print(f'Pontuação: {pontuacao}')