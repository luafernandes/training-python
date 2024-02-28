preco = float(input('Qual é o preço do produto? R$'))
novo_preco = preco - (preco * 5 / 100)
print('O novo valor será de R${:.2f}'.format(novo_preco))