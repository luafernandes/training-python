# Considerando US$1,00 = R$4,97
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.97
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))