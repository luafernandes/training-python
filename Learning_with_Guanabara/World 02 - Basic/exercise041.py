from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')