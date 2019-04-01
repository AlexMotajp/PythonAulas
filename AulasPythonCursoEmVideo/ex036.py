# Crie um programa que avalie possibilidade de emprestimo pra um cliente em um banco.
# Vai receber o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do slário do cliente.

salarioCliente = float(input('Insira o seu salário aqui: R$'))
casaValorTotal = float(input('Insira o valor da casa total aqui: R$'))
anosDePrestação = float(input('Insira em quantos anos ele vai pagar: '))

calculoPrestação = casaValorTotal / (anosDePrestação * 12)

if calculoPrestação <= (salarioCliente * 0.30):
    print('Você pode fazer o emprestimo!')
else:
    print('Você não pode fazer o emprestimo!')

