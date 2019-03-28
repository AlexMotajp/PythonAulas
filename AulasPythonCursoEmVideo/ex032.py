# Receba o ano, e diga se ele é bissexto ou não

ano = int(input('Insira o ano aqui: '))

if ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))

elif (ano % 4 == 0) and (ano % 100 != 0):
    print('O ano {} é bissexto'.format(ano))

else:
    print('O ano {} não é Bissexto'.format(ano))