# Problema 1021 do Beecrowd - Notas e Moedas

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for nota in notas:
    n = int(valor/nota)
    print('{} nota(s) de R$ {:.2f}'.format(n, nota))
    valor -= n * nota

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("MOEDAS:")
for moeda in moedas:
    n = int(round(valor,2)/moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(n, moeda))
    valor = round(valor - n * moeda, 2)