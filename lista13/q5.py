# print(sorted([input("Digite um nome: ") for i in range(10)]))

nomes = [input("Digite um nome: ") for i in range(10)]

print()
print("Em ordem alfabética:")
print(*sorted(nomes), sep=", \n")