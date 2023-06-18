def ehTriangular(x):
  i = 0
  while i * (i+1) * (i+2) < n:
    i += 1
  return i * (i+1) * (i+2) == n

n = int(input("Digite um número natural: "))

while n >= 0:
  print(f'{n} {"é" if ehTriangular(n) else "não é"} triangular')
  n = int(input("Digite um número natural: "))