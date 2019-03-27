# Crie um programa que receba o nome de uma cidade
# E diga se ela começa com 'SANTO'

cidade = input('Insira o nome da cidade: ')

cidadeAlterada = cidade.title()

if cidadeAlterada[0:5] == 'Santo':
    print('Essa cidade começa com Santo. A cidade é: {}'.format(cidadeAlterada))

