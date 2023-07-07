def fib(n, x=0, y=1):
  if n == 1:
    return y
  return fib(n-1, y, x+y)

# def fib(i):
#  if i == 1 or i == 2:
#    return 1
#  return fib(i-1) + fib(i-2)
  
n = int(input("Digite um inteiro: "))

while n > 0:
  print(fib(n))
  n = int(input("Digite um inteiro: "))
