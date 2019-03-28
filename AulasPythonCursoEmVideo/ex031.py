# Receba a distância de uma viagem em Km.
# Calcule o valor da passagem de R$0,50 por cada Km até 200Km
# e R$0,45 para viagens a cima de 200Km

viagemKm = float(input('Digite um valor em Km: '))

if viagemKm <= 200:
    print('Sua viagem vai custar: R${:.2f}'.format(viagemKm * 0.50))
else:
    print('Sua viagem vai custar: R${:.2f}'.format(viagemKm * 0.45))