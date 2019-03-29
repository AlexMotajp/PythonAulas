# Escreva um programa que receba salário de um funcionário
# Em seguida cacule o valor do seu aumento
# para salários a cima de 1.250,00 calcule 10%
# para inferior calcule 15%

varSal = float(input('Insira seu salário aqui: '))

if varSal > 1250:
    print('Seu salário agora é: R${:.2f}'.format(varSal * 1.10))
else:
    print('Seu salário agora é: R${:.2f}'.format(varSal * 1.15))
