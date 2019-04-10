# Leia um numero inteiro, e diga se é um número primo

numPri = int(input('Insira um valor inteiro: '))
totalNum = 0

for con in range(1, numPri + 1):
    if numPri % con == 0:
        print('\033[33m', end='')
        totalNum += 1
    else:
        print('\033[m', end='')
    print('{} '.format(con), end='')
print()
if totalNum > 2:
    print('O Número {} não é Primo!'.format(numPri))
else:
    print('O Número {} é Primo'.format(numPri))

