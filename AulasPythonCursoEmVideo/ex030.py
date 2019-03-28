# Crie um programa que receba um número, e diga se é par ou impar

varNum = int(input('Digite um valor inteiro: '))

if varNum % 2 == 0:
    print('O número {} é par '.format(varNum))
else:
    print('O número {} é impar'.format(varNum))
