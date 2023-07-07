def ehPar(x):
  return not x%2

n = int(input("Digite um número inteiro: "))

print(f'{n} é par' if ehPar(n) else f'{n} não é par')