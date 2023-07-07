# Problema 1012 do Beecrowd - Área

A, B, C = list(map(lambda n: float(n), input().split()))

pi = 3.14159
areaTriangulo = A*C/2
areaCirculo = pi*(C**2)
areaTrapezio = (A+B)*C/2
areaQuadrado = B**2
areaRetangulo = A*B

print('TRIANGULO: {:.3f}'.format(areaTriangulo))
print('CIRCULO: {:.3f}'.format(areaCirculo))
print('TRAPEZIO: {:.3f}'.format(areaTrapezio))
print('QUADRADO: {:.3f}'.format(areaQuadrado))
print('RETANGULO: {:.3f}'.format(areaRetangulo))