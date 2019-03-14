# Escreva um programa que receba Km percorridos de um carro
# e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmCarro = float(input('Quantos Km percorridos? '))
diasCarro = float(input('Quantos dias alugados? '))

calculando = (kmCarro * 0.15) + (diasCarro * 60)

print('o valor a ser pago: R${:.2f}'.format(calculando))
