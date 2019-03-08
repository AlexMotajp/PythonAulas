# Faça um programa que leia um num inteiro e mostre a tabuada do mesmo

numInteiro = int(input('Digite um valor inteiro: '))

print('Tabuada do {0}'.format(numInteiro))
for iterator in range(1, 11):
    multiplica = numInteiro * iterator
    print('{0} x {1} = {2}'.format(numInteiro, iterator, multiplica))

