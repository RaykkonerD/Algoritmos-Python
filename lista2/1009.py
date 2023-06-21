# Problema 1009 do Beecrowd - Salário com Bônus

funcionario = str(input())
salarioFixo = float(input())
vendasEfetuadas = float(input())
salario = salarioFixo + 0.15 * vendasEfetuadas

print('TOTAL = R$ {:.2f}'.format(salario))