# Problema 1239 do Beecrowd - Atalhos Bloggo

while True:
    try:
        texto = input()
        atalhos = ''
        abreI = True
        abreB = True
        
        for l in texto:
            if l == "_":
                atalhos += '<i>' if abreI else '</i>'
                abreI = not abreI
            elif l == "*":
                atalhos += '<b>' if abreB else '</b>'
                abreB = not abreB
            else:
                atalhos += l
        
        print(atalhos)
    except EOFError:
        break