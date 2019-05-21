# Faça um programa que receba o ano de nascimento de 7 pessoas, e diga quantas chegaram a maioridade
# e quantas ainda não chegaram

people01 = int(input('Digite o ano de nascimento: '))
people02 = int(input('Digite o ano de nascimento: '))
people03 = int(input('Digite o ano de nascimento: '))
people04 = int(input('Digite o ano de nascimento: '))
people05 = int(input('Digite o ano de nascimento: '))
people06 = int(input('Digite o ano de nascimento: '))
people07 = int(input('Digite o ano de nascimento: '))

vetorPeople = [people01, people02, people03, people04, people05, people06, people07]
contMaior = 0
contMenor = 0

for i in vetorPeople:
    if i < 2001:
        contMaior += 1

    elif i >= 2001:
        contMenor += 1

print('O número de pessoas que Atingiram a maioridade: {}'.format(contMaior))
print('O número de pessoas que NÃO atingiram a maioridade: {}'.format(contMenor))