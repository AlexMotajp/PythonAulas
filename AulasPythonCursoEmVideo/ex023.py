# Faça um programa que leia um número de 0 a 9999 e mostre na cada um dos
# digitos separados

varNum = (input('Digite um valor numero entre 0 e 9999: '))

misturando = varNum.split()

print(misturando)

if misturando[3]:
    print('Unidade: {}'.format(misturando[3]))
if misturando[2]:
    print('Dezena: {}'.format(misturando[2]))
if misturando[1]:
    print('Centena: {}'.format(misturando[1]))
if misturando[0]:
    print('Milhar {}'.format(misturando[0]))

