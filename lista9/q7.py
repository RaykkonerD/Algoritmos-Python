num = int(input("Digite um número inteiro: "))
i = 0
calculo = 0

while calculo < num and i != num:
  calculo = i * (i + 1) * (i + 2)
  i += 1

print(f"{num} {calculo != num and 'não é' or 'é'} triangular!")