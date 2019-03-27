# Faça um programa que mostre que recba o nome, mostre o primeiro e o ultimo

varName = input('Digite um nome aqui: ')

varName = varName.strip()
varName = varName.split()


print('Primeiro nome: {}'.format(varName[0]))
print('Último nome: {}'.format(varName[-1]))