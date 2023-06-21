# Problema 1254 do Beecrowd - Substituição de Tag

import re

while True:
    try:
        tagTitle = input()
        newTagTitle = input()
        code = input()

        posInicial = code.find("<")

        while posInicial != -1:
            posFinal = code.find(">", posInicial + 1)
            tag = code[posInicial:posFinal+1]
            newTag = re.sub(tagTitle, newTagTitle, tag, flags=re.IGNORECASE)
            code = code.replace(tag, newTag)
            posInicial = code.find("<", posInicial + len(newTag))

        print(code)
    except EOFError:
        break