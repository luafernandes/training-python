salario = float(input('Qual é o salário do funcionário? R$'))
novo_salario =  salario + (salario * 15 / 100)
print('O novo salário será de R${:.2f}'.format(novo_salario))