# Existem 4 alunos dispostos em sala, o professor quer sortear um deles pra apagar o quadro
# Crie um programa que leia o nome e imprima um aleatório

import random

aluno1 = input('Insira seu nome: ')
aluno2 = input('Insira seu nome: ')
aluno3 = input('Insira seu nome: ')
aluno4 = input('Insira seu nome: ')

randomVar = random.choice([aluno1, aluno2, aluno3, aluno4])

print('O escolhido foi: {}'.format(randomVar))

