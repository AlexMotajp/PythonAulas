# Crie um programa que leia duas notas de um aluno
# E calcule a média do mesmo
# Media abaixo de 5 reprovado, entre 5 e 6.9 final e 7 ou superior aprovado

nota01 = float(input('Digite sua primeira nota: '))
nota02 = float(input('Digite sua segunda nota: '))

media = (nota01 + nota02) / 2

if media < 5.0:
    print('Sinto muito, mas sua media é {:.1f}. Você foi Reprovado!'.format(media))
elif media == 5.0 or media <= 6.9:
    print('Você quase conseguiu, sua media atual é {:.1f}. Logo, você vai pra Final!'.format(media))
else:
    print('Parabéns sua media é {}. Você foi Aprovado!'.format(media))

