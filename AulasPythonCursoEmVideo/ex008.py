# Faça um programa que leia em metros e exiba convertido em cm e mm

metroNum = float(input('Digite o valor em metros que queira converter: '))

convCm = metroNum * 100
convMm = convCm * 10

print('O valor em cm é: {0:.2f} e o valor em mm: {1:.2f}'.format(convCm, convMm))
