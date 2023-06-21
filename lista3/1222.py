# Problema 1222 do Beecrowd - Concurso de Contos

while True:
	try:
		n, linhas, chars = list(map(lambda a : int(a), input().split()))
		conto = input()
		contoQuebrado = conto.split()
		caracteres = 0
		linhasFinais = 1 
		
		for palavra in contoQuebrado:
			tamanho = len(palavra)
			if caracteres == 0:
				caracteres = tamanho
			elif (caracteres + tamanho + 1) <= chars: 
				caracteres += tamanho + 1
			else: 
				linhasFinais += 1
				caracteres = tamanho
		
		print((linhasFinais+linhas-1) // linhas) 
	except EOFError:
		break