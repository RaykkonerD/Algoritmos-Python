def fatorial(x):
  if x == 0:
    return 1
  return x*fatorial(x-1)
  
n = int(input("Digite um natural qualquer: "))
while n >= 0:
  print(fatorial(n))
  n = int(input("Digite um natural qualquer: "))