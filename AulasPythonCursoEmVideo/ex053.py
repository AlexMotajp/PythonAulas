# Faça um programa que receba uma frase ou palavra e diga se é um palíndromo

palaVar = input('Insira uma palavra: ')
palaVar = palaVar.replace(' ','')

palaInv = palaVar[::-1]

print(palaInv)


if palaVar.title() == palaInv.title():
    print('A palavra é um Palíndromo!'.format(palaVar.title()))
else:
    print('A palavra não é um Palíndromo!'.format(palaVar.title()))
