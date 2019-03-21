# Faça um programa que receba um ângulo
# em seguida, imprima o valor do seno, cosseno e tangente de ângulo

from math import cos, sin, tan

angulo = int(input('Digite o valor do ângulo: '))

cosVar = cos(angulo)
senVar = sin(angulo)
tanVar = tan(angulo)

print('O Conseno desse angulo é: {}'.format(cosVar))
print('O Seno desse angulo é: {}'.format(senVar))
print('A tangente desse angulo é: {}'.format(tanVar))

