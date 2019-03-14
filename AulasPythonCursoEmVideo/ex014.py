# escreva um programa que converta uma temperatura digitada em °C para °F

celsiusVar = float(input("Insira o valor em Celsius para converter: °"))

print('O valor em Celsius: {:.2f} em Fahrenheit: {:.2f}'.format(celsiusVar, (celsiusVar * 9/5) + 32))