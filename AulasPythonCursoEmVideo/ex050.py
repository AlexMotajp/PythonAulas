# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas dos pares

numPar1 = int(input('Digite um valor: '))
numPar2 = int(input('Digite um valor: '))
numPar3 = int(input('Digite um valor: '))
numPar4 = int(input('Digite um valor: '))
numPar5 = int(input('Digite um valor: '))
numPar6 = int(input('Digite um valor: '))

listNum = [(numPar1), (numPar2), (numPar3), (numPar4), (numPar5), (numPar6)]

soma = 0
for c in listNum:
    if c % 2 == 0:
        print('Esses são os pares: {}'.format(c))
        soma += c
print('Soma de todos os pares: {}'.format(soma))
