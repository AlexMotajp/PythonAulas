# Programa que leia duas notas de um aluno e calcula a média

nota01 = float(input('Digite sua primeira nota: '))
nota02 = float(input('Digite sua segunda nota: '))

media = (nota01 + nota02)/2
mediaPond = ((nota01 * 4) + (nota02 * 6))/10

print('A media do aluno é: {0:.2f}, a media ponderada: {1:.2f}'.format(media, mediaPond))
