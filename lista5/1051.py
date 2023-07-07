# Problema 1051 do Beecrowd - Imposto de Renda

salario = float(input())

if salario <= 2000:
    print("Isento")
else:
    naoisento08 = salario - 2000
    naoisento018 = salario - 3000
    naoisento028 = salario - 4500
        
    if salario <= 3000:
        irpf = 0.08 * naoisento08
    elif salario < 4500:
        irpf = 80 + 0.18 * naoisento018
    else:
        irpf = 350 + 0.28 * naoisento028
    print('R$ %.2f' % irpf)