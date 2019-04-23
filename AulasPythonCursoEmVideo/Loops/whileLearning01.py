# Aprendendo While
# Calculadora simples

# Functions
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return  a / b


opcao = 0
while opcao != 5:
    print('=-' * 10)
    print('Calculadora Simples')
    print('=-' * 10)

    print('1- Soma')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    print('5- Sair')
    opcao = int(input('Digite o Número da Opção: '))


    if opcao == 1:
        num01 = float(input('Digite um número: '))
        num02 = float(input('Digite outro número: '))
        print('O valor da Soma: {:.2f}'.format(soma(num01, num02)))
    elif opcao == 2:
        num01 = float(input('Digite um número: '))
        num02 = float(input('Digite outro número: '))
        print('O valor da Subtração: {:.2f}'.format(sub(num01, num02)))
    elif opcao == 3:
        num01 = float(input('Digite um número: '))
        num02 = float(input('Digite outro número: '))
        print('O valor da Multiplicação: {:.2f}'.format(mult(num01, num02)))
    elif opcao == 4:
        num01 = float(input('Digite um número: '))
        num02 = float(input('Digite outro número: '))
        print('O valor da Divisão: {:.2f}'.format(div(num01, num02)))
    elif opcao != 5:
        print('Digite uma opcao válida')

print('Você saiu do Programa!')



