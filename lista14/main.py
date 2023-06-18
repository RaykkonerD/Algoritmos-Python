
# Cria uma nova matriz

def matriz(lin, col):
  matrizA = []
  
  for i in range(lin):
    linha = input(f'linha {i+1} >> ').split()
    while len(linha) != col:
      print(f'[ERRO]: NÚMERO DE COLUNAS DIFERENTE DO ESPERADO -> {col}')
      linha = input(f'linha {i+1} >> ').split()
    matrizA.append(linha)
    
  return matrizA


# Multiplica matrizes

def multiplica(matrizA, matrizB):
  return [[sum([float(A[i][k])*float(B[k][j]) for k in range(len(A[i]))]) for j in range(len(B[0]))] for i in range(len(A))]


# Multiplica matriz e escalar

def multiplicaEscalar(matrizA, esc):
  matrizR = [[float(valor) * esc for valor in linhaA] for linhaA in matrizA]
  return matrizR


# Calcula o determinante

def determinante(matrizA, ordem):
  a = [[float(n) for n in linha] for linha in matrizA]
  
  if ordem == 1:
    return a[0][0]
    
  elif ordem == 2:
    dPrincipal = a[0][0] * a[1][1]
    dSecundaria = a[0][1] * a[1][0]
    return dPrincipal - dSecundaria 
    
  elif ordem == 3:
    dPrincipal = 0
    
    for i in range(3):
      mult = 1
      for j in range(3):
        mult *= a[j][i+j < len(a) and i+j or i+j-3]
      dPrincipal += mult 
    
    dSecundaria = 0
    
    for i in range(3):
      mult = 1
      for j in range(3):
        mult *= a[j][i-j]
      dSecundaria += mult 

    return dPrincipal - dSecundaria 
    
    

# Menu de operações

print('======= Operações com matrizes =========')
print()
print('1 - multiplicação entre matrizes')
print('2 - multiplicação entre matriz e escalar')
print('3 - determinante')
print()

op = int(input('Opção: '))

print('--------------------------------')
print()

# Primeira matriz

linhasA, colunasA = map(int, input('Dimensões da matriz A (lxc): ').split('x'))

if op != 3:
  A = matriz(linhasA, colunasA)
  print(*A, sep="\n")
  print()
  
  if op == 1:
    # Segunda matriz
    linhasB, colunasB = map(int, input('Dimensões da matriz B (lxc): ').split('x'))
    B = matriz(linhasB, colunasB)
    print(*B, sep="\n")
    print()
  
    if colunasA == linhasB:
      print()
      print('[RESULTADO]:')
      print()
      
      print(*multiplica(A, B), sep="\n")
    else:
      print('[ERRO]: O número de colunas da primeira matriz deve ser equivalente ao número de linhas da segunda matriz !!')
      
  elif op == 2:
    escalar = float(input('Digite o número escalar: '))
    
    print()
    print()
    print('[RESULTADO]:')
    print()
    
    print(*multiplicaEscalar(A, escalar), sep="\n")
  
else:
  while linhasA != colunasA or linhasA > 3:
    print('[ERRO]: Deve ser uma matriz quadrada !!' if linhasA != colunasA else '[ERROR]: Ordem da matriz excede 3 !!', end='\n\n')
    linhasA, colunasA = map(int, input('Dimensões da matriz A (lxc): ').split('x'))
  
    
  A = matriz(linhasA, colunasA)
  print(*A, sep="\n")
  
  print()
  print()
  print('[RESULTADO]:')
  print()
  
  print(f'D = {determinante(A, linhasA)}', sep="\n")