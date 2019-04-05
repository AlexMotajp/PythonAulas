# Crie um programa que faça o computador jogar Jokenpô com você

from random import choice

suaPosicao = input('Pedra, Papel ou Tesoura? ')
compPosicao = str(choice(['Pedra', 'Papel', 'Tesoura']))

suaPosicao = suaPosicao.title()
compPosicao = compPosicao.title()

if suaPosicao == compPosicao:
    print('Você empatou. Você escolheu: {} e o Computador: {}'.format(suaPosicao, compPosicao))
elif suaPosicao == 'Pedra':
    if compPosicao == 'Papel':
        print('Você Perdeu! Você Escolheu: {} e o Computador: {}'.format(suaPosicao, compPosicao))
    else:
        print('Você Venceu! Você escolheu: {} e o Computador: {}'.format(suaPosicao, compPosicao))
elif suaPosicao == 'Papel':
    if compPosicao == 'Pedra':
        print('Você Venceu! Você escolheu: {} e o Computador: {}'.format(suaPosicao, compPosicao))
    else:
        print('Você Perdeu! Você escolheu: {} e o Computador: {}'.format(suaPosicao, compPosicao))
elif suaPosicao == 'Tesoura':
    if compPosicao == 'Papel':
        print('Você Venceu! Você escolheu: {} e o Computador: {}'.format(suaPosicao, compPosicao))
    else:
        print('Você Perdeu! Você escolheu: {} e o Computador: {}'.format(suaPosicao, compPosicao))

