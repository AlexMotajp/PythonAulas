# Laços...
# Mexendo inicilamente com For

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print('Found a number', num)

# para criar um laço, começa escrevendo for 'controlador' in range (começo, tamanho)
# o in range, como já diz é a range, a quantidade de execuções daquele laço

# Exemplos
for c in range(1, 6):
    print(c)
print('')

# contratar de trás pra frente, coloque os numero de tras pra frente, e no fim coloque o 3 parametro com -1

for c in range(6, 0, -1):
    print(c)
print('')

# o ultimo parametro pode ser um "saltador" para o contrlador também. pular de 2 em 2:
for c in range(0, 11, 2):
    print(c)
