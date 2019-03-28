
varNum = (input('Insira um valor entre 0 e 9999: '))

if varNum[0:1]:
    print('Milhar: {}'.format(varNum[0:1]))
if varNum[1:2]:
    print('Centena {}'.format(varNum[1:2]))
if varNum[2:3]:
    print('Dezena: {}'.format(varNum[2:3]))
if varNum[3:4]:
    print('Unidade: {}'.format(varNum[3:4]))

# Outra forma de fazer o exercício ex23