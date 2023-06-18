x, y = map(float, input("Digite os números separados por espaço: ").split())

while x or y:
  print(x+y)
  x, y = map(float, input("Digite os números separados por espaço: ").split())

print("2 entradas 0. Execução finalizada.")