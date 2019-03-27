# Crie um programa que receba um nome de uma pessoa
# E diga se no nome existe Silva.

nomePeople = input('Insira o nome aqui: ')

nomeAlterado = nomePeople.title()

if nomeAlterado.find("Silva") or nomeAlterado[0:5] == ("Silva"):
    print('Esse nome tem Silva! O nome é {}'.format(nomeAlterado))

# você também poderia usar o in do python
# 'Silva' in nomeAlterado.title()