# mexendo com tipos
# veja que estou convertendo tudo que está em n1 em inteiro
# caso não seja colocado o conversor int, ele vai concatenar as strings e não somar

n1 = int(input('Digite um valor: '));
n2 = int(input('Digite outro valor: '));

soma = n1 + n2;
print('A soma entre {0} e {1} vale: {2}'.format(n1, n2, soma));
# perceba como é interessante o format


