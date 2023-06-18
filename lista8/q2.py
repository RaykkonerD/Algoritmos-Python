palavra = input("Digite uma palavra: ").upper();
nA = 0;
nE = 0;
nI = 0;
nO = 0;
nU = 0;

for letra in palavra:
  match letra:
    case "A":
      nA += 1;
    case "E":
      nE += 1;
    case "I":
      nI += 1;
    case "O":
      nO += 1;
    case "U":
      nU += 1;

print(f"A: {nA}, E: {nE}, I: {nI}, O: {nO}, U: {nU}");

# print(f"A: {palavra.count('A')}, E: {palavra.count('E')}, I: {palavra.count('I')}, O: {palavra.count('O')}, U: {palavra.count('U')}");