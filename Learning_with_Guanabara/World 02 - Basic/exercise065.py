c = 1
num = int(input('Digite um número: '))
r = input('Quer continuar? [S/N] ')
soma = maior = menor = num
while r in 'Ss':
    num = int(input('Digite um número: '))
    r = input('Quer continuar? [S/N] ')
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    c += 1
media = soma / c
print('Você digitou {} números \nA média entre eles foi {:.2f} \nO menor valor foi {} e o maior valor foi {}.'.format(c, media, menor, maior))
