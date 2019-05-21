# Faça um programa que receba nome, idade e sexo de 4 pessoas.
# Depois mostre a média de idade do grupo, nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

idadeTotal = 0
idadeMaiorHomem = 0
nomeMaiorIdade = ''
contMulher = 0

for cont in range(1, 5):
    print('----- {}º Pessoa -----'.format(cont))
    namePeople = input('Digite o nome da pessoa: ')
    agePeople = int(input('Diga sua idade: '))
    sexoPeople = input('Qual sexo? M ou F: ')
    idadeTotal += agePeople
    if sexoPeople == 'M' and agePeople > idadeMaiorHomem:
        idadeMaiorHomem = agePeople
        nomeMaiorIdade = namePeople
    if agePeople < 20 and sexoPeople in 'fF':
        contMulher += 1

print('Media da idade do Grupo: {}'.format(idadeTotal / 4))
print('Nome do Homem mais velho: {}'.format(nomeMaiorIdade))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(contMulher))