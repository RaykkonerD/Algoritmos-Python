string = input("Digite a string: ")
maisRecorrente = ''
nOcorrencias = 0

for c in string:
  nc = 0
  for d in string:
    if d == c:
      nc += 1

  if nc > nOcorrencias:
    nOcorrencias = nc
    maisRecorrente = c

print(f'Caracter que mais ocorre: "{maisRecorrente}"')
print(f'Número de ocorrências: {nOcorrencias}')