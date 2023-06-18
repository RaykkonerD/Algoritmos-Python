for num in range(300, 501):
  i = 0
  calculo = 0
  
  while calculo != num and i != num:
    calculo = i * (i + 1) * (i + 2)
    i += 1
  
  if i != num:
    print(num)

