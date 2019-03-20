# Faça um programa que leia cateto oposto e adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa
# Teorema de Pitágoras

from math import pow, sqrt

catetoOp = float(input('Digite o cateto Oposto: '))
catetoAd = float(input('Digite o cateto Adjacente: '))

hipotenusa = sqrt(pow(catetoOp, 2) + pow(catetoAd, 2))

print('O comprimento da hipotenusa é: {}'.format(hipotenusa))



