maior = 0;
menor = None;
media = 0;

for i in range(5):
  n = int(input());
  if i == 0 or n < menor:
    menor = n;
  
  if n > maior:
    maior = n;

  media += n;

media /= 5;

print(f'Menor: {menor}');
print(f'Maior: {maior}');
print(f'Média: {media:.2f}');
    
# nums = [int(input()) for i in range(30)];

# print(f'Menor: {min(nums)}');
# print(f'Maior: {max(nums)}');
# print(f'Média: {(sum(nums)/len(nums)):.2f}');