turma = []

for aluno in range(1, 41):
  entrada = input(f"Digite as médias do aluno {aluno} separadas por espaço: ").split()
  notasAluno = list(map(float, entrada))
  mediaAluno = sum(notasAluno)/len(notasAluno)

  turma.append(mediaAluno)
  print(mediaAluno)

print(sum(turma)/len(turma))