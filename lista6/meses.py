mes = input("Digite o nome do  mês: ");

match mes:
  case 'Janeiro' | 'Março' | 'Maio' | 'Julho' | 'Agosto' | 'Outubro' | 'Dezembro':
    print(f'O mês de {mes} tem 31 dias.');
  case 'Abril' | 'Junho' | 'Setembro' | 'Novembro':
    print(f'O mês de {mes} tem 30 dias.');
  case 'Fevereiro':
    print('O mês de Fevereiro tem 28 dias.');
  case _:
    print('MÊS INVÁLIDO!!');