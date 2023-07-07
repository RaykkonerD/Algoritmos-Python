mediaAnualDaTurma = 0;

for aluno in range(40):
  nota1 = float(input("Digite a 1* média bimestral: "));
  nota2 = float(input("Digite a 2* média bimestral: "));
  nota3 = float(input("Digite a 3* média bimestral: "));
  nota4 = float(input("Digite a 4* média bimestral: "));

  mediaAnualAluno = (nota1 + nota2 + nota3 + nota4) / 4;
  print(f'Média do aluno {aluno+1}: {mediaAnualAluno}');
  mediaAnualDaTurma += mediaAnualAluno;

mediaAnualDaTurma /= 40

print(f'Média da turma: {mediaAnualDaTurma}');
