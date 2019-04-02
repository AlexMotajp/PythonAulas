# Escreva um programa que leia dois números inteiros
# e compare pra saber qual é o maior e o menor
# é pra ser dito se forem iguais também

varNum01 = int(input('Digite o primeiro número: '))
varNum02 = int(input('Digite o segundo número: '))

if varNum01 > varNum02:
    print('O primeiro número {} é maior que o segundo {}'.format(varNum01, varNum02))
elif varNum02 > varNum01:
    print('O segundo número {} é maior que o primeiro {}'.format(varNum02, varNum01))
else:
    print('Ambos são iguais {} e {}'.format(varNum01, varNum02))