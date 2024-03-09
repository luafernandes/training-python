soma = c = 0
while True:
    num = int(input('Digite um número ou 999 para parar: '))
    if num == 999:
        break
    soma += num
    c += 1
print('Você digitou {} números e a soma entre eles é igual a {}.'.format(c, soma))
