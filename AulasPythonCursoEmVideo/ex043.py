# Desenvolva um programa que receba altura e peso
# Calcule seu IMC
# e mostre os seu status

alturaPessoa = float(input('Digite sua altura em cm: '))
pesoPessoa = float(input('Digite seu peso: '))

alturaPessoa = alturaPessoa * 0.01
altPow = pow(alturaPessoa, 2)

imc = pesoPessoa / altPow

if imc < 18.5:
    print('Seu IMC: {:.1f}. Você está abaixo do Peso!'.format(imc))
elif imc >= 18.5 or imc < 25:
    print('Seu IMC é {:.1f}. Você está no Peso Normal!'.format(imc))
elif imc >= 25 or imc < 30:
    print('Seu IMC é {:.1f}. Você está no Sobrepeso!'.format(imc))
elif imc >= 30 or imc < 35:
    print('Seu IMC é {:.1f}. Você está Obeso Grau 1!'.format(imc))
elif imc >= 35 or imc < 40:
    print('Seu IMC é {:.1f}. Você está Obeso Grau 2!'.format(imc))
else:
    print('Seu IMC é {:.1f}. Você está Obeso Grau 3!'.format(imc))



