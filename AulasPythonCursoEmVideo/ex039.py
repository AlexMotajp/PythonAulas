# Faça um programa que leia o ano de nascimento
# E diga de acordo com sua idade:
# 1 - vai se aista ainda, 2 - Se é a hora de se alistar, 3 - Se já passou do tempo de alistamento
from datetime import date

dataNascimento = int(input('Digite o ano do seu nascimento: '))


strDate = str(date.today().year)
strDate = int(strDate.replace('-',''))
idade = strDate - dataNascimento

if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print('Ainda não é obrigado a se alistar!')
else:
    print('Passou da hora de se alistar!')