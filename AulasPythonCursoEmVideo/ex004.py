# Faça um programa que leia algo pelo teclado e retorne seu tipo primitivo + outras informações

varQualquer = input('Digite alguma coisa: ')


print(type(varQualquer))
print('digito: ',varQualquer.isdigit())
print('identificador: ',varQualquer.isidentifier())
print('numerico: ',varQualquer.isnumeric())
print('alphanumeric: ',varQualquer.isalnum())
print('sem caps lock: ',varQualquer.islower())
print('caps lock: ',varQualquer.isupper())
print('titlecase: ',varQualquer.istitle())
