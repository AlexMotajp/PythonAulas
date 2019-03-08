# Faça um programa que leia largura, altura em metros
# Calcule a área, e a quantidade de tinta necessária para pintá-la
# Levando em conta que cada litro de tinta, pinta uma área de 2m^2

varLarg = float(input('Insira o valor da largura: '))
varAltura = float(input('Insira o valor da altura: '))

areaCalc = varAltura * varLarg
tintaCalc = areaCalc / 2

print('O valor da Área é: {0:.2f}, será necessário {1:.2f} litros de tinta'.format(areaCalc, tintaCalc))



