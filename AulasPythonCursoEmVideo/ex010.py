# Crie um programa que leia quantos reias uma pessoa tem, e quantos dolares ela pode comprar

receitaDaPessoa = float(input('Digite o valor em R$ que você tem: '))

convertDolar = receitaDaPessoa * 0.26

print('Você tem R$ {0:.2f} e pode comprar U$ {1:.2f}'.format(receitaDaPessoa, convertDolar))