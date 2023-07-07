indexSemana = int(input("Digite o número do dia da semana: "))

match indexSemana:
  case 2 | 3 | 4 | 5 | 6:
    print('Dia Ùtil!');
  case 1 | 7:
    print('Fim de semana!');
  case _:
    print('ENTRADA INVÁLIDA!!');