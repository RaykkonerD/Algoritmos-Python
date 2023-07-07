# Problema 1064 do Beecrowd - Positivos e Média

pos = 0
average = 0

for i in range(6):
    number = input()
    if float(number) >= 0:
        average += float(number)
        pos += 1

average /= pos

print(f'{pos} valores positivos')
print('%.1f' % average)