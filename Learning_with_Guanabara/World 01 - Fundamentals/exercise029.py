v = float(input('Digite a sua velocidade: '))
if v > 80:
    print('Multado! Você excedeu o limite de 80km/h')
    multa = (v-80)*7
    print('O valor da multa é de R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança')