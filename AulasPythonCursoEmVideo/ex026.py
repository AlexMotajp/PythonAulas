# Receba uma Frase e Mostre quantidade de A,
# posição que ela aparece pela primeira vez e a última posição

fraseVar = input('Insira uma frase aqui: ')

fraseCap = fraseVar.upper()
fraseCap = fraseCap.strip()

print('A quantidade de "a" é: {}'.format(fraseCap.count('A')))

print('O  primeiro "a", aparece na posição: {}'.format(fraseCap.find('A') + 1))

print('A última posição que o "a" aparece é: {}'.format(fraseCap.rfind('A') + 1))
