# Fazer um programa que receba um numero fracional e mostr sua porção inteira

from math import ceil,floor
numFrac = float(input('Digite um valor decimal: '))

print('O valor inteiro de {} é: {}'.format(numFrac, floor(numFrac)))

