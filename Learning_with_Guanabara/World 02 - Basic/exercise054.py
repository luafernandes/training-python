from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for p in range(1,8):
    ano_nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E tivemos {} pessoas menores de idade.'.format(menor))
