# Faça um programa que receba um ângulo
# em seguida, imprima o valor do seno, cosseno e tangente de ângulo

from math import cos, sin, tan, radians

angulo = float(input('Digite o valor do ângulo: '))



cosVar = cos(radians(angulo))
senVar = sin(radians(angulo))
tanVar = tan(radians(angulo))

print('O Cosseno desse angulo é: {:.2f}'.format(cosVar))
print('O Seno desse angulo é: {:.2f}'.format(senVar))
print('A tangente desse angulo é: {:.2f}'.format(tanVar))

