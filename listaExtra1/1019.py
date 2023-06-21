# Problema 1019 do Beecrowd - Conversão de Tempo

tempo = int(input())
resto = tempo
horas = int(resto/3600)
resto -= horas*3600
minutos = int(resto/60)
resto -= minutos*60
segundos = resto

print('{}:{}:{}'.format(horas,minutos,segundos))