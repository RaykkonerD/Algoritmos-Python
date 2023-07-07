while True:
  x = float(input("Digite um número real qualquer: "))
  y = float(input("Digite outro número real qualquer: "))
  
  if not x and not y:
    break
    
  print(f'Soma: {x+y}')