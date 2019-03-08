# Crie um algoritimo que mostre Dobro, triplo e raiz quadrada dele

numQualquer = float(input('Insira um valor numerico: '))

dobroNum = numQualquer * 2
triploNum = numQualquer * 3
raizNum = numQualquer ** (1/2)

print('O Dobro: {0:.0f}, O Triplo: {1:.0f} e a Raiz: {2:.1f}'.format(dobroNum, triploNum, raizNum))