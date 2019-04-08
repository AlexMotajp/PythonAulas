# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três.
# No intervalo entre 1 até 500

print('Todos os números ímpares entre 1 e 500')

for c in range(1, 500):
    if c % 3 == 0:
        soma = 0
        soma = soma + c
        print('O número múltiplo de 3: {}'.format(c))
print('A soma dos impares múltiplos de 3 é: {}'.format(soma))

