# O mesmo professor quer decidir a ordem de alunos que irão apresentar um trabalho
# Faça um programa que receba o nome e gere uma ordem

import random

aluno1 = input('Insira seu nome: ')
aluno2 = input('Insira seu nome: ')
aluno3 = input('Insira seu nome: ')
aluno4 = input('Insira seu nome: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)

print('A ordem de apresentação será: ')
print('Primeiro: {}'.format(alunos[0]))
print('Segundo: {}'.format(alunos[1]))
print('Terceiro: {}'.format(alunos[2]))
print('Quarto: {}'.format(alunos[3]))




