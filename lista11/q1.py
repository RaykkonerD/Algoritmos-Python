def intervalo(x, y):
  if x > y:
    for i in range(x, y-1, -1):
      print(i)
  else:
    for j in range(x, y+1):
      print(j)

n1, n2 = map(int, input("Digite os limites superior e inferior, separados por espaço: ").split())

while n1 != 0 or n2 != 0:
  intervalo(n1, n2)
  n1, n2 = map(int, input("Digite os limites superior e inferior, separados por espaço: ").split()) 