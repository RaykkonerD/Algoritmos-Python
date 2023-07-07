# Problema 1072 do Beecrowd - Intervalo 2

n = int(input())
ins = 0
outs = 0

for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        ins += 1
    else:
        outs += 1
        
print(f'{ins} in')
print(f'{outs} out')