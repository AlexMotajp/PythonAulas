# Crie um programa que leia o nome completo de uma pessoa e mostrar:
# - Imprima tudo maiúsculo, - tudo minúsculo
# - quantas letras sem considerar espaços
# - quantas letras tem o primeiro nome

namePeople = input('Insira seu nome completo: ')

print('Minúscula: {}'.format(namePeople.lower()))
print('Maiúscula: {}'.format(namePeople.upper()))

print('Tamanho sem Considerar espaços: {}'.format(len(namePeople.replace(' ',''))))

firstName = namePeople.split()[0]
print('Tamanho do primeiro nome: {}'.format(len(firstName)))


