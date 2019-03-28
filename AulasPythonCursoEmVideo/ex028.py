# Faça um programa que receba o número entre 0 e 5
# e compare com um random do computador. Se baterem, o usuário acertou, se não ele errou.

from random import randrange

print('Adivinha o número que estou pensando!')
varUser = int(input('Insira um valor entre 0 e 5: '))

randomPc = randrange(0, 5)

if randomPc == varUser:
    print('Você acertou. O número é: {}'.format(randomPc))
else:
    print('Você errou! O número era: {}'.format(randomPc))

