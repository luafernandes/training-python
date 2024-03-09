num = 0
soma = 0
c = 0
while num != 999:
    num = int(input('Digite um número ou 999 para parar: '))
    if num != 999:
        soma += num
        c += 1
    else:
        print('Programa finalizado! Calculando...')
print('Você digitou {} números e a soma entre eles é igual a {}.'.format(c, soma))