# Crie um programa que receba 5 pesos, e diga qual maior e menor deles.

peso01 = float(input('Digite o Primeiro peso: '))
peso02 = float(input('Digite o Segundo peso: '))
peso03 = float(input('Digite o Terceiro peso: '))
peso04 = float(input('Digite o Quarto peso: '))
peso05 = float(input('Digite o Quinto peso: '))

listPeso = [peso01, peso02, peso03, peso04, peso05]

print('Esse é o MAIOR peso: {:.2f}'.format(max(listPeso)))
print('Esse é o MENOR peso: {:.2f}'.format(min(listPeso)))

