# Problema 1018 do Beecrowd - Cédulas

valor = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for cedula in cedulas:
    notas = int(valor/cedula)
    print('{} nota(s) de R$ {},00'.format(notas, cedula))
    valor -= notas*cedula