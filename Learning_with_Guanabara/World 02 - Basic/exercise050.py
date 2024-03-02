soma = 0
for c in range(1,7):
    num = int(input('Digite o {}° número inteiro: '.format(c)))
    if num % 2 == 0:
        soma += num
print('\nA soma entre os números digitados é igual a {}.'.format(soma))
