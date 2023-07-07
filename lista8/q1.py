palavra = input("Digite uma palavra: ").upper();
quantB = 0;
quantC = 0;
quantD = 0;

for letra in palavra:
  if letra == 'B':
    quantB += 1;
  elif letra == 'C':
    quantC += 1;
  elif letra == 'D':
    quantD += 1;

print(f"B: {quantB}, C: {quantC}, D: {quantD}");

# print(f"B: {palavra.count('B')}, C: {palavra.count('C')}, D: {palavra.count('D')}");