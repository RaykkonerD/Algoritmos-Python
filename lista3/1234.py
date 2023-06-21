# Problema 1234 do Beecrowd - Sentença Dançante

while True:
    try:
        sentenca = input()
        sentencaDancante = ''
        eh = True
        
        for l in sentenca:
            if l.isalpha():
                if eh:
                    sentencaDancante += l.upper()
                else:
                    sentencaDancante += l.lower()
                eh = not eh
            else:
                sentencaDancante += l
        
        print(sentencaDancante)
    except EOFError:
        break