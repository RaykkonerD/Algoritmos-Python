DNA = input('Insira a sequência do DNA: ')
complemento = ''

for base in DNA:
  novaBase = ''
  if base == 'A':
    novaBase = 'T'
  elif base == 'C':
    novaBase = 'G'
  elif base == 'G':
    novaBase = 'C'
  elif base == 'T':
    novaBase = 'A'
    
  complemento = novaBase + complemento

print(f'Complemento reverso: {complemento}')
