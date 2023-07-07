# Problema 1020 do Beecrowd - Idade em Dias

idade = int(input())
anos = int(idade/365)
idade -= anos*365
meses = int(idade/30)
idade -= meses*30
dias = idade

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))