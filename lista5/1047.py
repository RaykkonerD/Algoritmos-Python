# Problema 1047 do Beecrowd - Tempo de Jogo com Minutos

h1, m1, h2, m2 = map(lambda a: int(a), input().split())
horatotal = h2 - h1;
minutototal = m2 - m1;

if minutototal < 0:
    horatotal -= 1
    minutototal += 60

if horatotal < 0:
    horatotal += 24
  
if horatotal == 0 and minutototal == 0:
    horatotal += 24
    

print(f"O JOGO DUROU {horatotal} HORA(S) E {minutototal} MINUTO(S)")