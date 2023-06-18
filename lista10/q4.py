string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
maiorSubstring = ''
stringComum = ''

for c in string1:
  if (stringComum + c) in string2:
    stringComum += c
    if len(stringComum) > len(maiorSubstring):
      maiorSubstring = stringComum
  else:
    stringComum = c

# print(f'Maior substring: {maiorSubstring}')
print(len(maiorSubstring))