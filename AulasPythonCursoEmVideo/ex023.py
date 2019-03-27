# Faça um programa que leia um número de 0 a 9999 e mostre na cada um dos
# digitos separados

varNum = int(input('Digite um valor numero entre 0 e 9999: '))

unidade = varNum // 1 % 10
dezena = varNum // 10 % 10
centena = varNum // 100 % 10
milhar  = varNum // 1000 % 10

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
