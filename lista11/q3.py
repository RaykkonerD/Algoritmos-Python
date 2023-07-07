def ehPrimo(x):
  for i in range(2, x):
    if x%i == 0:
      return False
  return True

n = int(input("Digite um número natural: "))

while n >= 0:
  print(f'{n} {"é" if ehPrimo(n) else "não é"} primo')
  n = int(input("Digite um número natural: "))