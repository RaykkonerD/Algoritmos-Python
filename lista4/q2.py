'''Escreva um algoritmo que calcule as raízes de uma equação do 2° grau, na forma ax2+bx+c.

O algoritmo deve pedir os valores de a, b e c e calcular as raízes.

• Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o algoritmo não deve pedir os demais valores. Deve encerrar a execução de imediato.

• ∆ = b² − 4ac.

• Se o ∆ calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre a execução.

• Se o ∆ for igual a zero a equação possui apenas uma raiz real. Informe-a ao usuário.

    x = −b/2a

• Se o ∆ for positivo, a equação possui duas raízes reais. Informe-as ao usuário.

    x = (−b ± √∆) / 2a'''


a = int(input())

if a:
  b = int(input())
  c = int(input())
  delta = b**2 -4*a*c
  
  if delta < 0:
    print("A equação não tem raízes reais!")
  elif delta == 0:
    print(f"A equação possui uma única raiz: {-b/(2*a)}")
  else:
    print("A equação possui duas raízes:")
    print(f"x': {(-b+(delta**(1/2)))/(2*a)}")
    print(f"x'': {(-b-(delta**(1/2)))/(2*a)}")
      
else:
    print("O elemento A = 0. Impossível calcular as raízes. (Não tem raízes reais)")