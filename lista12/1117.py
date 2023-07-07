# Problema 1117 do Beecrowd -	Validação de Nota

n = float(input())
soma = None

while soma == None or n < 0 or n > 10:
    if n > 10 or n < 0:
        print('nota invalida')
    else:
        soma = n
    n = float(input())
    
soma += n
media = soma / 2

print('media = %.2f' % media)