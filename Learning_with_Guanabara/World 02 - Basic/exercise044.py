print('{:=^40}'.format(' Simulador de Loja '))
preco = float(input('Qual o valor total da compra? R$'))
print(''' \nFormas de Pagamento
[1] Dinheiro / Cheque
[2] Cartão à vista
[3] Cartão em até 2x (SEM JUROS)
[4] Cartão 3x ou mais (COM JUROS)\n''')
opcao = int(input('Qual a forma de pagamento desejada? '))
if opcao == 1:
    valor = preco - (preco * 10 / 100)
elif opcao == 2:
    valor = preco - (preco * 5 / 100)
elif opcao == 3:
    valor = preco
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    valor = preco + (preco * 20 / 100)
    quant_parcela = int(input('Quantas parcelas? '))
    parcela = valor / quant_parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(quant_parcela, parcela))
else:
    valor = preco
    print('Opção de pagamento inválida, escolha entre 1 e 4!')
print('Sua compra de R${} vai custar R${} no final.'.format(preco, valor))
