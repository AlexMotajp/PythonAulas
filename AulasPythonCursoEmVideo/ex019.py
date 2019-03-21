# Existem 4 alunos dispostos em sala, o professor quer sortear um deles pra apagar o quadro
# Crie um programa que leia o nome e imprima um aleatório

import random

aluno1 = input('Insira seu nome: ')
aluno2 = input('Insira seu nome: ')
aluno3 = input('Insira seu nome: ')
aluno4 = input('Insira seu nome: ')

varRandom = random.randint(1,4)

print(varRandom)

if varRandom == 1:
    print('O escolhido foi você: {}'.format(aluno1))
elif varRandom == 2:
    print('O escolhido foi você: {}'.format(aluno2))
if varRandom == 3:
    print('O escolhido foi você: {}'.format(aluno3))
elif varRandom == 4:
    print('O escolhido foi você: {}'.format(aluno4))