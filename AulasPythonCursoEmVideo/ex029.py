# Crie um programa que verifique a velocidade de um carro
# Caso a velocidade ultrapasse 80Km/h, Diga que ele foi multado
# Imprima também o valor da multa, que equivale a R$7,00 por Km excedido

varKm = float(input('Insira o Km/h aqui: '))

if varKm > 80:
    print('Você ultrapassou o limite de velocidade permitido.')
    print('Sua multa é de R${:.2f}:'.format((varKm - 80) * 7))

