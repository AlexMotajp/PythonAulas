# Aula de manipulação de Caracteres

varTexto = 'Aulas com o curso em vídeo'

print(len(varTexto))
# Identificando o tamanho da String

print(varTexto[15:])

# usando count

print(varTexto.count('o'))
# analisando a quantidades de o dentro da string


# posso também colocar a posição dos caracteres
print(varTexto.count('o',0,13))

#identificando em que posição se encontra um caracter ou um conjunto de caracteres dentro da string

print(varTexto.find('vídeo'))
# Se for retornado -1, lembre-se que isso significa que a string não existe

# Transformando

print(varTexto.replace('curso', 'python'))
# alterando a string curso para python

print(varTexto.title())
# É feito um capitalize em todos as palavras separadas por espaço

print(varTexto.strip())
# Ele remove todas os espaço vazios excedentes no começo e fim da string
# da pra escolher apenas um lado... lstrip() ou rstrip()

print(varTexto.split())
# ele gera uma lista com todas as palavras da string

# vamos criar uma var, pra receber esa string alterada pelo split

stringAlterada = varTexto.split()

print('-'.join(stringAlterada))
# o join, une onde foi separado a string.




