valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Qual o salário do comprador? R$'))
tempo = int(input('Em quantos anos gostaria de pagar? '))

prestacao = valor / (tempo * 12)
minimo = salario * (30/100)

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, tempo), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo autorizado!')
else:
    print('Empréstimo negado!')
