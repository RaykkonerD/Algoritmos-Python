DNA = input('Insira a sequência do DNA: ')
RNA = ''

for base in DNA:
  RNA += base == 'T' and 'U' or base

print(f'RNA correspondente: {RNA}')

# print(f'RNA correspondente: {DNA.replace("T", "U")}')