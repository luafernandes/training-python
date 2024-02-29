dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
pago = (60 * dia) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(pago))