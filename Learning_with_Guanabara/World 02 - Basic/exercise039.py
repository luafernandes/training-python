from datetime import date
ano_nasc = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('Se você nasceu em {}, você tem {} anos.'.format(ano_nasc, idade))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    falta = 18 - idade
    print('Você ainda não precisa se alistar, faltam {} anos para o alistamento.'.format(falta))
    ano_alist = ano_atual + falta
    print('Seu alistamento será em {}.'.format(ano_alist))
elif idade > 18:
    falta = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(falta))
    ano_alist = ano_atual - falta
    print('Seu alistamento foi em {}.'.format(ano_alist))
