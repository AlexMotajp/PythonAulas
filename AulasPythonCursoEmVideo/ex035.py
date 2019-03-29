# Receba três valores de comprimento e diga se eles podem formar um triângulo

a = float(input('Insira o comprimento da primeira reta: '))
b = float(input('Insira o comprimento da segunda reta: '))
c = float(input('Insira o comprimento da terceira reta: '))

if ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b)):
    print('A união das retas: {:.2f}, {:.2f} e {:.2f} podem formar um triângulo'.format(a, b, c))
else:
    print('Sinto, mas essas retas: {:.2f}, {:.2f}, {:.2f} não podem formar um triângulo'.format(a, b, c))

