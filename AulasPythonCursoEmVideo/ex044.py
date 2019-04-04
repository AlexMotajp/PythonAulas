# Crie uma programa que receba o valor de um produto
# Considerando o seu preço normal e condição de pagamento
# - A vista dinheiro/cheque: 10% de desconto
# - A vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

valorProduto = float(input('Insira o valor do produto: '))
formaPag = int(input('- 1 Á vista no Dinheiro (desconto de 10%) \n'
                 '- 2 Á vista no Cheque (desconto de 10%) \n'
                 '- 3 Á vista no Cartão (desconto de 5%) \n'
                 '- 4 Em até 2x no Cartão (preço normal) \n'
                 '- 5 3x ou mais no Cartão (20% de juros) \n'
                 'Qual forma de pagamento (entre 1 e 5): ' ))

if formaPag == 1:
    print('Á vista no dinheiro o produto ficou no valor de: R${:.2f}'.format(valorProduto * 0.90))
elif formaPag == 2:
    print('Á vista no cheque o produto ficou no valor de: R${:.2f}'.format(valorProduto * 0.90))
elif formaPag == 3:
    print('Á vista no cartão o produto ficou no valor de: R${:.2f}'.format(valorProduto * 0.95))
elif formaPag == 4:
    print('2x no cartão o produto ficou no valor de: R${:.2f} com parcelas: R${}'.format(valorProduto, valorProduto / 2))
elif formaPag == 5:
    xNoCar = int(input('Quantos vezes no cartão: '))
    print('Você dividiu em {}x no Cartão o valor total: R${:.2f} com parcelas: R${:.2f}'.format(xNoCar,
                                                                    valorProduto * 1.20, (valorProduto * 1.2) / xNoCar))
else:
    print('Você digitou uma opção incorreta! Tente outra vez.'.format())
