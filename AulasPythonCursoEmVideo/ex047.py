# Crie um programa que mostre na tela todos os números pares entre 1 e 50

for c in range(1, 50):
    if c % 2 == 0:
        print('Número par: {}'.format(c))

print('Acabou!')