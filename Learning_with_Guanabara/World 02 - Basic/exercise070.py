print('='*25)
print('{:^25}'.format('DESCRIÇÃO DE COMPRAS'))
print('='*25, end='\n')
c = 1
cont = ' '
preco_total = prod_mais_1000 = menor_preco = total_prod = 0
prod_barato = ''
while True:
    print(f'{c}º PRODUTO')
    nome_prod = input('Digite o nome do produto: ').strip().capitalize()
    preco = float(input('Digite o preço: R$'))
    total_prod += 1
    if total_prod == 1 or preco < menor_preco:
        menor_preco = preco
        prod_barato = nome_prod
    preco_total += preco
    if preco > 1000:
        prod_mais_1000 += 1
    cont = input('Quer adicionar mais produtos? [S/N] ').strip().upper()
    while cont not in 'SN':
        cont = input('Entrada inválida. Quer adicionar mais produtos? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
    c += 1
    print('='*25)
print('='*25)
print(f'O preço total da compra foi de R${preco_total:.2f}.')
print(f'No total {prod_mais_1000} produtos custam mais de R$1000,00.')
print(f'O produto mais barato é {prod_barato} que custa R${menor_preco:.2f}.')