# Problema 1060 do Beecrowd - Números positivos

ints = 0

while True:
    try:
        number = input()
        if number.isdecimal():
            ints += 1
    except EOFError:
        break

print(f'{ints} valores positivos')