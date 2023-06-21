# Problema 1015 do Beecrowd - Distância Entre Dois Pontos

p1 = input().split(' ')
p2 = input().split(' ')
x1, y1 = list(map(lambda a: float(a), p1))
x2, y2 = list(map(lambda a: float(a), p2))
distancia = ((x2-x1)**2+(y2-y1)**2)**(1/2)

print('{:.4f}'.format(distancia))