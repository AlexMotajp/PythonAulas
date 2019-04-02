# Receba um número inteiro e converta em uma base de conversão Binário, Octal ou Hexadecimal
# Mas antes, pergunta a o usuário qual deles ele quer

numInt = int(input('Insira um valor inteiro para que possa ser Convertido: '))
ctr = int(input('- 1 para Binário /n - 2 para Octal /n - 3 para Hexadecimal: '))

if ctr == 1:
    print('O valor de {} em Binário é: {}'.format(numInt, bin(numInt)))
elif ctr == 2:
    print('O valor de {} em Octal é: {}'.format(numInt, oct(numInt)))
elif ctr == 3:
    print('O valor em Hexadecimal é: {}'.format(numInt, hex(numInt)))
else:
    print('Escolha incorreta. Tente um número válido entre 1 e 3!')
