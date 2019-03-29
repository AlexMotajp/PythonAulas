# Faça um programa que receba 3 números e diga qual é o maior e menor entre eles

num01 = int(input('Insira um número: '))
num02 = int(input('Insira outro numero: '))
num03 = int(input('Insira mais um: '))

menorValue = num01
maiorValue = num01

# Menor valor
if num02 < num01 and num02 < num01:
    menorValue = num02
if num03 < num01 and num03 < num01:
    menorValue = num03

print('Esse é o manor valor: {}'.format(menorValue))

# Maior vlaor
if num02 > num01 and num02 > num01:
    maiorValue = num02
if num03 > num01 and num03 > num01:
    maiorValue = num03

print('Esse é o maior valor: {}'.format(maiorValue))



