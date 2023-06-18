for num in range(200, 300):
  divisor = num - 1
  divisao = num%divisor
    
  while divisao:
    divisor -= 1
    divisao = num%divisor
  
  if divisor == 1:
    print(num)