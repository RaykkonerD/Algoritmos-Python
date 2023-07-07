def ehPrimo(x):
  for i in range(2, x):
    if not x%i:
      return False
      break
  return True

count = 0
p = 2
lista = []

while count < 100:
  if ehPrimo(p):
    count += 1
    lista.append(p)
  p += 1

print(lista, sum(lista))