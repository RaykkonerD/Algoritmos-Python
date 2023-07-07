def soma(lista):
  soma = 0
  for n in lista:
    soma += n 
  return soma

li = int(input("Digite o limite inferior: "))
lf = int(input("Digite o limite superior: "))
lista = []

for i in range(li, lf+1):
  lista.append(i**2)

print(*lista, sep=", ")
print(soma(lista))