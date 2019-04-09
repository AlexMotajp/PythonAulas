# Desenvolva um programa que leia um termo número
# após isso uma razão, e produza uma progressão aritimética
# No fim, mostre os 10 primeiros termos

digitNum = int(input('Digite o termo inicial: '))
digitRaz = int(input('Digite a razão: '))
formProg = digitNum + (11 - 1) * digitRaz

somaProg = 0
print('-=-' * 10)
print('Progressão Aritmética')
print('-=-' * 10)

for c in range(digitNum, formProg, digitRaz):
    print('Progressão: {}'.format(c))

print('Acabou!')
