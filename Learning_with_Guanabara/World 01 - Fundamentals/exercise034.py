salario = float(input('Qual o salário do funcionário? R$'))
if salario > 1250:
    novo_salario = salario + (salario * (10/100))
else:
    novo_salario = salario + (salario * (15/100))
print('Quem ganhava R${}, passa a ganhar R${:.2f}'.format(salario, novo_salario))