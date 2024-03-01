nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('A média foi de {:.2f}.'.format(media))
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('A média foi de {:.2f}.'.format(media))
    print('RECUPERAÇÃO')
else:
    print('A média foi de {:.2f}.'.format(media))
    print('APROVADO')