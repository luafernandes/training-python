#OPÇÃO 01
dist = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de {}Km'.format(dist))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print('O valor da passagem será R${:.2f}'.format(preco))

#OPÇÃO 02
dist = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de {}Km'.format(dist))
preco = dist * 0.5 if dist <= 200 else dist * 0.45
print('O valor da passagem será R${:.2f}'.format(preco))
