# Faça um programa que receba 3 números e diga qual é o maior e menor entre eles

num01 = int(input('Insira um número: '))
num02 = int(input('Insira outro numero: '))
num03 = int(input('Insira mais um: '))

if (num01 > num02) and (num01 > num03):
    print('O primeiro numero {} é o maior de todos'.format(num01))
else:
    print('O número {} mais baixo'.format(num01))