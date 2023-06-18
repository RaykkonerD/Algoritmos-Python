primos = 0
num = 2

while primos < 100:
  divisor = num - 1
  divisao = num%divisor
    
  while divisao:
    divisor -= 1
    divisao = num%divisor
  
  if divisor == 1:
    print(num)
    primos += 1
  num += 1