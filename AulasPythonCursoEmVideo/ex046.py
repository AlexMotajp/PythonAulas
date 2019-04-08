# Faça um programa que mostre na tela contagem regressiva de 10 a 0
# de fogos de artíficios com pausa de 1 segundo.

from time import sleep

print('-=' * 15)
print('Contagem Reressiva dos Fogos!')
print('-=' * 15)

for c in range(10, -1, -1):
    print(c)
    sleep(1)

