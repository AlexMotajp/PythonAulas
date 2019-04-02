# Receba o ano de nascimento de um atleta e mostre sua categoria
# - Até 9 anos mirim
# - Até 14 anos Infantil
# - Até 19 anos Junior
# - Até 20 anos Sênior
# - Acima é Master

from datetime import date

anoDoParticipante = int(input('Digite seu ano de nascimento: '))

anoAtual = str(date.today().year)
idadeDoPart = int(anoAtual) - anoDoParticipante

if idadeDoPart <= 9:
    print('Você tem {} anos. Logo, Categoria Mirim!'.format(idadeDoPart))
elif idadeDoPart <= 14:
    print('Você tem {} anos. Logo, Categoria Infantil!'.format(idadeDoPart))
elif idadeDoPart <= 19:
    print('Você tem {} anos. Logo, Categoria Junior!'.format(idadeDoPart))
elif idadeDoPart == 20:
    print('Você tem {} anos. Logo, Categoria Sênior'.format(idadeDoPart))
else:
    print('Você tem {} anos. Logo, Categoria Master'.format(idadeDoPart))

